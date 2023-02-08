def create_db_bronze():

    from sqlalchemy import create_engine 
    from sqlalchemy import Column, String, Integer, Float, ForeignKey
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker

    import os


    try:
        os.remove("db_bronze.sqlite")
        print('Base de données bronze supprimée.')
    except:
        print('Pas de base de données bronze.')


    global engine
    engine = create_engine("sqlite:///db_bronze.sqlite", echo=True)
    global base
    base = declarative_base()


    class Customers (base):

        __tablename__ = "Customers"

        customer_id = Column(String(255), nullable=False, primary_key=True)
        customer_unique_id = Column(String(255))
        customer_zip_code_prefix = Column(Integer())
        customer_city = Column(String(255))
        customer_state = Column(String(255))

        def __init__(self, customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state):

            self.customer_id = customer_id
            self.customer_unique_id = customer_unique_id
            self.customer_zip_code_prefix = customer_zip_code_prefix
            self.customer_city = customer_city
            self.customer_state = customer_state



    class Geolocations (base):

        __tablename__ = "Geolocations"

        index = Column(Integer(), nullable=False, primary_key=True)
        geolocation_zip_code_prefix = Column(Integer())
        geolocation_lat = Column(Float())
        geolocation_lng = Column(Float())
        geolocation_city = Column(String(255))
        geolocation_state = Column(String(255))

        def __init__(self, index, geolocation_zip_code_prefix, geolocation_lat, geolocation_lng, geolocation_city, geolocation_state):

            self.index = index
            self.geolocation_zip_code_prefix = geolocation_zip_code_prefix
            self.geolocation_lat = geolocation_lat
            self.geolocation_lng = geolocation_lng
            self.geolocation_city = geolocation_city
            self.geolocation_state = geolocation_state



    class Order_items (base):

        __tablename__ = "Order_items"

        index = Column(Integer(), nullable=False, primary_key=True)
        order_id = Column(String(255))
        order_item_id = Column(Integer())
        product_id = Column(String(255))
        seller_id = Column(String(255))
        shipping_limit_date = Column(String(255))
        price = Column(Float())
        freight_value = Column(Float())

        def __init__(self, index, order_id, order_item_id, product_id, seller_id, shipping_limit_date, price, freight_value):

            self.index = index
            self.order_id = order_id
            self.order_item_id = order_item_id
            self.product_id = product_id
            self.seller_id = seller_id
            self.shipping_limit_date = shipping_limit_date
            self.price = price
            self.freight_value = freight_value



    class Order_payments (base):

        __tablename__ = "Order_payments"

        index = Column(Integer(), nullable=False, primary_key=True)
        order_id = Column(String(255))
        payment_sequential = Column(Integer())
        payment_type = Column(String(255))
        payment_installments = Column(Integer())
        payment_value = Column(Float())

        def __init__(self, index, order_id, payment_sequential, payment_type, payment_installments, payment_value):

            self.index = index
            self.order_id = order_id
            self.payment_sequential = payment_sequential
            self.payment_type = payment_type
            self.payment_installments = payment_installments
            self.payment_value = payment_value



    class Order_reviews (base):

        __tablename__ = "Order_reviews"

        index = Column(Integer(), nullable=False, primary_key=True)
        review_id = Column(String(255))
        order_id = Column(String(255))
        review_comment_title = Column(String(255))
        review_comment_message = Column(String(255))
        review_creation_date = Column(String(255))
        review_answer_timestamp = Column(String(255))
        review_score = Column(Integer())

        def __init__(self, index, review_id, order_id, review_score, review_comment_title, review_comment_message, review_creation_date, review_answer_timestamp):

            self.index = index
            self.review_id = review_id
            self.order_id = order_id
            self.review_comment_title = review_comment_title
            self.review_comment_message = review_comment_message
            self.review_creation_date = review_creation_date
            self.review_answer_timestamp = review_answer_timestamp
            self.review_score = review_score



    class Order_dataset (base):

        __tablename__ = "Order_dataset"

        order_id = Column(String(255), nullable=False, primary_key=True)
        customer_id = Column(String(255))
        order_status = Column(String(255))
        order_purchase_timestamp = Column(String(255))
        order_approved_at = Column(String(255))
        order_delivered_carrier_date = Column(String(255))
        order_delivered_customer_date = Column(String(255))
        order_estimated_delivery_date = Column(String(255))

        def __init__(self, order_id, customer_id, order_status, order_purchase_timestamp, order_approved_at, order_delivered_carrier_date, order_delivered_customer_date, order_estimated_delivery_date):

            self.order_id = order_id
            self.customer_id = customer_id
            self.order_status = order_status
            self.order_purchase_timestamp = order_purchase_timestamp
            self.order_approved_at = order_approved_at
            self.order_delivered_carrier_date = order_delivered_carrier_date
            self.order_delivered_customer_date = order_delivered_customer_date
            self.order_estimated_delivery_date = order_estimated_delivery_date



    class Products_dataset (base):

        __tablename__ = "Products_dataset"

        product_id = Column(String(255), nullable=False, primary_key=True)
        product_category_name = Column(String(255))
        product_name_lenght = Column(Float())
        product_description_lenght = Column(Float())
        product_photos_qty = Column(Float())
        product_weight_g = Column(Float())
        product_length_cm = Column(Float())
        product_height_cm = Column(Float())
        product_width_cm = Column(Float())

        def __init__(self, product_id, product_category_name, product_name_lenght, product_description_lenght, product_photos_qty, product_weight_g, product_length_cm, product_height_cm, product_width_cm):

            self.product_id = product_id
            self.product_category_name = product_category_name
            self.product_name_lenght = product_name_lenght
            self.product_description_lenght = product_description_lenght
            self.product_photos_qty = product_photos_qty
            self.product_weight_g = product_weight_g
            self.product_length_cm = product_length_cm
            self.product_height_cm = product_height_cm
            self.product_width_cm = product_width_cm



    class Sellers_dataset (base):

        __tablename__ = "Sellers_dataset"

        seller_id = Column(String(255), nullable=False, primary_key=True)
        seller_zip_code_prefix = Column(Integer())
        seller_city = Column(String(255))
        seller_state = Column(String(255))

        def __init__(self, seller_id, seller_zip_code_prefix, seller_city, seller_state):

            self.seller_id = seller_id
            self.seller_zip_code_prefix = seller_zip_code_prefix
            self.seller_city = seller_city
            self.seller_state = seller_state



    class Category_names (base):

        __tablename__ = "Category_names"

        product_category_name = Column(String(255), nullable=False, primary_key=True)
        product_category_name_english = Column(String(255), nullable=False)

        def __init__(self, product_category_name, product_category_name_english):

            self.product_category_name = product_category_name
            self.product_category_name_english = product_category_name_english





    base.metadata.create_all(engine)

