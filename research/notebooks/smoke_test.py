"""Check that the research image can import its tools, read the data and train a model."""

from pathlib import Path

import lightgbm as lgb
import numpy as np
import polars as pl
import scipy
import sklearn
import statsmodels


def main() -> None:
    """Print tool versions, row counts per data file and the result of a tiny LightGBM fit."""
    print(f"polars={pl.__version__} scipy={scipy.__version__} sklearn={sklearn.__version__}")
    print(f"statsmodels={statsmodels.__version__} lightgbm={lgb.__version__}")

    files = sorted(Path("/work/data").glob("*.jsonl"))
    assert files, "no data files mounted at /work/data"
    for path in files:
        print(f"{path.name}: {pl.read_ndjson(path).height} rows")

    rng = np.random.default_rng(0)
    features = rng.random((200, 3))
    labels = (features[:, 0] > 0.5).astype(int)
    model = lgb.LGBMClassifier(n_estimators=10, verbose=-1).fit(features, labels)
    print(f"lightgbm train accuracy={model.score(features, labels):.2f}")
    print("smoke test passed")


if __name__ == "__main__":
    main()
