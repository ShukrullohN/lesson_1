def create_table():
    category = """
    create table category(
        category_id serial primary key,
        name varchar(20),
        last_update  date default now());
    """
    country = """
    create table country(
        country_id serial primary key,
        name varchar(20),
        create_date date default now()); 
    """
    product = """
    create table product(
        product_id serial primary key,
        name varchar(20),
        price numeric,
        made int references country(country_id),
        category_id int references category(category_id),
        create_date date default now());
    """
    wants = """
    create table wants(
        want_id serial primary key,
        product_id int references product(product_id),
        last_update date default now());
    """
    customer = """
    create table customer(
        customer_id serial primary key,
        first_name varchar(20),
        last_name varchar(20),
        email varchar(30),
        password varchar(20),
        want_id int references wants(want_id),
        create_date date default now());
    """
    seller = """
    create table seller(
        seller_id serial primary key,
        first_name varchar(20),
        last_name varchar(20),
        email varchar(30),
        password varchar(20),
        product_id int references product(product_id),
        create_date date default now());
    """
    order = """
    create table order(
        order_id serial primary key,
        product_id int references product(product_id),
        customer_id int references customer(customer_id),
        status varchar(20),
        last_update date default now());
    """
    payment = """
    create table payment(
        payment_id serial primary key,
        product_id int references product(product_id),
        customer_id int references customer(customer_id),
        card_number varchar(20),
        last_update date default now());
    """
    adress = """
    create table adress(
        adress_id serial primary key,
        name varchar(20),
        last_update date default now();
    """
    deliveries = """
    create table deliveries(
        deliveries_id serial primary key,
        product_id int references product(product_id),
        customer_id int references customer(customer_id),
        adress_id int references adress(adress_id),
        date date default now());
    """
    data = {
        "category": category,
        "country": country,
        "product": product,
        "wants": wants,
        "customer": customer,
        "customer": customer,
        "order": order,
        "payment": payment,
        "adress": adress,
        "deliveries": deliveries
    } 
    for i in data:
        print(f"{i} {Database.connect(data[i], "create")}")


if __name__ == "__main__":
    create_table()