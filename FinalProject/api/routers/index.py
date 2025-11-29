from . import orders, order_details, recipes, payment_details, sandwiches, users, resources


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(recipes.router)
    app.include_router(payment_details.router)
    app.include_router(sandwiches.router)
    app.include_router(users.router)
    app.include_router(resources.router)

