from ontap_oop.filefactory import FileFactory
from ontap_oop.product import Product

# Tạo danh sách sản phẩm ban đầu
p1 = Product(1, "Coca", 100)
dataset = []
dataset.append(p1)
dataset.append(Product(2,"Pepsi", 20))
dataset.append(Product(3,"Sting", 80))
dataset.append(Product(4,"Aqua", 70))
dataset.append(Product(5,"Redbull", 50))
print("Danh sách sản phẩm: ")
for product in dataset:
    print(product)

while True:
    id = int(input("Nhập mã: "))
    name = input("Nhập tên: ")
    price = float(input("Nhập giá: "))
    p = Product(id, name, price)
    dataset.append(p)
    ask = input("Nhập tiếp không? (c/k): ")
    if ask == 'k':
        break
print("Danh sách sản phẩm sau khi nhập: ")
for product in dataset:
    print(product)
#Lọc sản phẩm theo giá từ a đến b
def filter_products_by_price(dataset, a, b):
    return [product for product in dataset if a <= product.price <= b]

#Xóa sản phẩm có giá nhỏ hơn x
def remove_products_below_x(dataset, x):
    return [product for product in dataset if product.price >= x]

# Tùy chọn một trong 2 chức năng
while True:
    print("\nChọn chức năng:")
    print("1. Lọc sản phẩm")
    print("2. Xóa sản phẩm")
    print("3. Thoát")
    choice = int(input("Lựa chọn của bạn: "))

    if choice == 1:
        a = float(input("Nhập giá a: "))
        b = float(input("Nhập giá b: "))
        filtered_products = filter_products_by_price(dataset, a, b)
        print("Danh sách sản phẩm trong khoảng giá từ", a, "đến", b, ":")
        for product in filtered_products:
            print(product)
    elif choice == 2:
        x = float(input("Nhập giá x: "))
        dataset = remove_products_below_x(dataset, x)
        print("Danh sách sản phẩm sau khi xóa các sản phẩm có giá nhỏ hơn", x, ":")
        for product in dataset:
            print(product)
    elif choice == 3:
        break
    else:
        print("Vui lòng chọn lại.")
# Gọi chức năng chụp ảnh đối tượng xuống ổ cứng
ff = FileFactory()
ff.writeData("mydataset.json", dataset)
print("Danh sách sản phẩm đã được lưu vào file mydataset.json")
