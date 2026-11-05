"""Build content with the original theme, excluding old published HTML/assets."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def main():
    root = Path(__file__).resolve().parents[1]
    builder = Path(sys.executable).with_name("jupyter-book")
    if not builder.exists():
        raise SystemExit("Install requirements.txt in this Python environment first.")

    # The repo contains both sources and an old published site. Building at its
    # root makes Jupyter Book treat published _static files as custom CSS/JS.
    # Stage only sources instead; no theme overrides or published files change.
    with tempfile.TemporaryDirectory(prefix="decal-book-source-") as directory:
        # Resolve macOS /var -> /private/var before MyST computes image paths.
        source = Path(directory).resolve()
        for name in ("_config.yml", "_toc.yml", "favicon.png", "LICENSE.md"):
            shutil.copy2(root / name, source / name)
        for name in ("chapters", "images", "data", "assets"):
            shutil.copytree(
                root / name, source / name,
                ignore=shutil.ignore_patterns("*.html", ".ipynb_checkpoints"),
            )
        subprocess.run(
            [str(builder), "build", str(source), "--all"],
            check=True,
        )
        # Build beside the staged notebooks so legacy MyST-NB image paths
        # resolve correctly, then copy the finished preview into the repo.
        shutil.copytree(source / "_build" / "html", root / "_build" / "html",
                        dirs_exist_ok=True)
        print(f"Preview: {root / '_build' / 'html'}")


if __name__ == "__main__":
    main()
