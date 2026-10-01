from browser import document # type: ignore

def SKU_generator(e):
    category = document.getElementById('category').value
    product_name = document.getElementById('product_name').value
    stock_qty = document.getElementById('quantity').value

    if not category:
        document.getElementById('sku_output').innerHTML = '<span class="text-red-500 font-sans text-xs">Please select a valid category.</span>'
        return

    prod_code = product_name[:4].upper() if product_name else "PROD"
    qty = str(stock_qty) if stock_qty else "0"

    sku = category[:3].upper() + "-" + prod_code + "-" + qty
    document.getElementById('sku_output').innerHTML = f"<strong>SKU:</strong>&nbsp;{sku}"

document["sku_btn"].bind("click", SKU_generator)
