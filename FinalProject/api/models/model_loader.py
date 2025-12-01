from . import orders, order_details, recipes, sandwiches, resources,users, payment_details, reviews, users

from ..dependencies.database import engine


def index():
    payment_details.Base.metadata.create_all(engine)
    users.Base.metadata.create_all(engine)
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)


