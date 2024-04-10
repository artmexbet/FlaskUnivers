from data.database import create_session, init
from data.__all_models import *

init()
session = create_session()
order = session.query(Order).first()
order.items.append(session.query(Item).first())
session.commit()
