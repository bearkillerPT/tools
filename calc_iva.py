
def getIvaValue(product_value, iva_value):
    return product_value * iva_value / 100

fist_purchase = 239.25
second_purchase = 199.93

iva_value = 23

first_purchase_iva = getIvaValue(fist_purchase, iva_value)
second_purchase_iva = getIvaValue(second_purchase, iva_value)

print("First purchase iva: ", round(first_purchase_iva, 2), "€ / ", round(fist_purchase, 2), "€")
print("Second purchase iva: ", round(second_purchase_iva, 2), "€ / ", round(second_purchase, 2), "€")

print("Total iva: ", round(first_purchase_iva + second_purchase_iva, 2), "€ / ", round(fist_purchase + second_purchase, 2), "€")