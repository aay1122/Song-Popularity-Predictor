def predict_popularity(features):
    tempo = features.get("tempo", 0)
    energy = features.get("energy", 0)
    danceability = features.get("danceability", 0)

    # Score formula
    score = (0.3 * tempo/200) + (0.4 * energy) + (0.3 * danceability)

    if score > 0.6:
        label = "🔥 Hit Song"
    elif score > 0.4:
        label = "👍 Average Song"
    else:
        label = "👎 Low Popularity"

    return label, round(score, 2)