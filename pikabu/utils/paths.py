def abs_path_from_project(relative_path: str):
    import pikabu
    from pathlib import Path

    return (
        Path(pikabu.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )