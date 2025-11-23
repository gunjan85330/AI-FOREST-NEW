import numpy as np
from sklearn.neighbors import KDTree

def run_simulation(df, model, lat, lon, steps, threshold):
    coords = df[["lat", "lon"]].values
    tree = KDTree(coords)

    dist = np.abs(df["lat"] - lat) + np.abs(df["lon"] - lon)
    start_idx = dist.idxmin()

    FEATURES = model.feature_names_in_

    burning = {start_idx}
    history = [burning.copy()]

    for _ in range(steps):
        new_fire = set()
        for cell in burning:
            _, neigh = tree.query([coords[cell]], k=50)
            for n in neigh[0][1:]:
                risk = model.predict_proba(df.loc[n, FEATURES].to_frame().T)[0][1]
                if risk > threshold:
                    new_fire.add(n)

        burning |= new_fire
        history.append(burning.copy())

    return history, len(burning)


