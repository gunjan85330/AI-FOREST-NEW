import numpy as np
from sklearn.neighbors import KDTree

def run_simulation(df, model, lat, lon, steps, threshold):

    # Ensure numeric data types for model
    FEATURES = list(model.feature_names_in_)

    for col in FEATURES:
        df[col] = df[col].astype(float)

    coords = df[["lat", "lon"]].astype(float).values
    tree = KDTree(coords)

    # find ignition point
    dist = np.abs(df["lat"] - lat) + np.abs(df["lon"] - lon)
    start_idx = dist.idxmin()

    burning = {start_idx}
    history = [burning.copy()]

    for _ in range(steps):
        new_fire = set()

        for cell in burning:
            # fetch 30 nearest neighbors
            _, neigh = tree.query([coords[cell]], k=30)

            for n in neigh[0][1:]:
                sample = df.loc[n, FEATURES].to_frame().T.fillna(0).astype(float)
                risk = model.predict_proba(sample)[0][1]

                if risk > threshold:
                    new_fire.add(int(n))

        burning |= new_fire
        history.append(burning.copy())

    return history, len(burning)



