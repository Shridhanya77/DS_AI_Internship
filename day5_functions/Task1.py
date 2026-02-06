def calc_rectangle(length,width):
    area=length*width
    perimeter=2*(length+width)
    return area,perimeter

length=float(input("Enter the length of a rectangle :"))
width=float(input("Enter width of reactangle : "))

area,perimeter=calc_rectangle(length,width)
print(f"Area of a rectangle : {area} \n Perimeter of a rectangle : {perimeter}")
