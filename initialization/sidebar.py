from core.utils.registry.side_navigation import register_sidebar_item, register_category

SIDEBAR_ITEMS = [
    {
        "name": "Content",
        "icon_type": "svg",
        "icon": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='currentColor' class='size-8 text-gray-500 border bg-white rounded-lg p-2 shadow'><path d='M3 3.5A1.5 1.5 0 0 1 4.5 2h6.879a1.5 1.5 0 0 1 1.06.44l4.122 4.12A1.5 1.5 0 0 1 17 7.622V16.5a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 3 16.5v-13Z' /></svg>",
        "route": "pages.contents",
        "roles": ["Administrator", "Editor"],
    }
]

CATEGORIES = [
    {
        "name": "Content Management",
        "roles": ["Administrator", "Editor"],
    }
]

def register_sidebar_items():
    for category in CATEGORIES:
        register_category(
            name=category["name"],
            roles=category["roles"]
        )

    for item in SIDEBAR_ITEMS:
        register_sidebar_item(
            name=item["name"],
            icon_type=item["icon_type"],
            icon=item["icon"],
            route=item["route"],
            roles=item["roles"],
            category_name="Content Management"
        )

