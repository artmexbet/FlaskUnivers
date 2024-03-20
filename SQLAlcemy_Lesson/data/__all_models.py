from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.sqlite import TEXT, INTEGER
from sqlalchemy.orm import relationship

from .database import Base


class Item(Base):
    __tablename__ = 'items'

    def __init__(self, title, price):
        super().__init__()
        self.title = title
        self.price = price

    id = Column(INTEGER, primary_key=True)
    title = Column(TEXT, unique=True)
    price = Column(INTEGER, nullable=False)

    orders = relationship("Order", secondary="orders_to_items",
                          backref="orders",
                          lazy="subquery")

    def __repr__(self):
        return f"Item('{self.title}')"


class Order(Base):
    __tablename__ = 'orders'

    def __init__(self, address):
        super().__init__()
        self.address = address

    id = Column(INTEGER, primary_key=True)
    address = Column(TEXT)

    items = relationship("Item", secondary="orders_to_items",
                         backref="items",
                         lazy="subquery")


class OrderItem(Base):
    __tablename__ = 'orders_to_items'

    id = Column(INTEGER, primary_key=True)
    order_id = Column(INTEGER, ForeignKey('orders.id'))
    item_id = Column(INTEGER, ForeignKey('items.id'))
    #
    # order = relationship('Order')
    # item = relationship('Item')
