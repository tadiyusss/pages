from core.utils.registry.side_navigation import register_sidebar_item, register_category
from core.utils.dashboard import DashboardItem, DashboardCategory

SIDEBAR = [
    DashboardCategory(
        name="Content Management",
        roles=["Administrator", "Editor"],
        items=[
            DashboardItem(
                name = "Category",
                icon_type = "svg",
                icon = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='currentColor' class='sidenav-item'><path fill-rule='evenodd' d='M4.5 2A2.5 2.5 0 0 0 2 4.5v2.879a2.5 2.5 0 0 0 .732 1.767l4.5 4.5a2.5 2.5 0 0 0 3.536 0l2.878-2.878a2.5 2.5 0 0 0 0-3.536l-4.5-4.5A2.5 2.5 0 0 0 7.38 2H4.5ZM5 6a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z' clip-rule='evenodd' /></svg>",
                route = "pages.category",
                roles = ["Administrator", "Editor"]
            ),
            DashboardItem(
                name="Contents",
                icon_type="svg",
                icon="<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='currentColor' class='sidenav-item'><path d='M3 3.5A1.5 1.5 0 0 1 4.5 2h6.879a1.5 1.5 0 0 1 1.06.44l4.122 4.12A1.5 1.5 0 0 1 17 7.622V16.5a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 3 16.5v-13Z' /></svg>",
                route="pages.contents",
                roles=["Administrator", "Editor"]
            ),
        ]
    )
]

def register_sidebar_items():
    for category in SIDEBAR:
        register_category(category)
