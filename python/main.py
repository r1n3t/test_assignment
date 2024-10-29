def analyze_availability(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = file.readlines()

    store_names = []
    product_availability = {}

    for line in data:
        if line.strip(): 
            store_name, products_info = line.split(':')
            store_name = store_name.strip()
            store_names.append(store_name)

            products = products_info.split(',')
            for product in products:
                product_name, quantity = map(str.strip, product.rsplit('-', 1))
                quantity = int(quantity)

                if product_name not in product_availability:
                    product_availability[product_name] = {'count': 0, 'stores': set()}

                if quantity > 0:
                    product_availability[product_name]['count'] += 1
                    product_availability[product_name]['stores'].add(store_name)

    threshold = len(store_names) / 2
    result = []

    for product, info in product_availability.items():
        if info['count'] >= threshold:
            missing_stores = sorted(set(store_names) - info['stores'])
            result.append((product, len(missing_stores), missing_stores))

    result.sort()

    with open(output_file, 'w', encoding='utf-8') as file:
        for product, missing_count, missing_stores in result:
            if missing_count > 0:
                file.write(f"{product} - {missing_count} [{', '.join(missing_stores)}]\n")

analyze_availability('input.txt', 'output.txt')