from dataclasses import dataclass


@dataclass
class DataSection:
    community: str
    hot: str


data_section = DataSection(
    community='Блоги компаний',
    hot='Горячие публикации'
)
