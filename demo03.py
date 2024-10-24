class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"名称: {self.name}, 价格: {self.price}, 库存: {self.stock}"


class SellingMachine:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        if not self.products:
            print("当前没有商品。")
            return
        print("当前商品列表:")
        for product in self.products:
            print(product)

    def add_stock(self, name, quantity):
        for product in self.products:
            if product.name == name:
                product.stock += quantity
                print(f"已为商品 '{name}' 添加了 {quantity} 个库存。")
                return
        print(f"未找到商品 '{name}'。")

    def sell_product(self, name, quantity, amount_paid):
        for product in self.products:
            if product.name == name:
                total_cost = product.price * quantity
                if amount_paid < total_cost:
                    print(f"金额不足，需支付 {total_cost} 元。")
                    return
                if product.stock < quantity:
                    print(f"库存不足，当前库存为 {product.stock}。")
                    return
                product.stock -= quantity
                change = amount_paid - total_cost
                print(f"销售成功！找零: {change} 元。")
                return
        print(f"未找到商品 '{name}'。")


# 示例使用
if __name__ == "__main__":
    machine = SellingMachine()

    # 添加商品
    machine.add_product(Product("可乐", 3.0, 10))
    machine.add_product(Product("薯片", 5.0, 5))
    machine.add_product(Product("巧克力", 2.5, 20))

    # 列出商品
    machine.list_products()

    # 添加库存
    machine.add_stock("可乐", 5)

    # 销售商品
    machine.sell_product("可乐", 3, 10.0)  # 足够金额
    machine.sell_product("薯片", 6, 30.0)  # 库存不足
    machine.sell_product("巧克力", 2, 4.0)  # 金额不足

    # 再次列出商品
    machine.list_products()
