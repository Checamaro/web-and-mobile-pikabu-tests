from dataclasses import dataclass


@dataclass
class DataSearch:
    python: str


data_search = DataSearch(
    python='Python'

)


@dataclass
class DataSearchWithFilter:
    tag: str


data_search_with_filter = DataSearchWithFilter(
    tag='Мемы'
)

@dataclass
class DataSection:
    community: str
    hot: str

data_section = DataSection(
    community='Все сообщества',
    hot='Горячее'
)
