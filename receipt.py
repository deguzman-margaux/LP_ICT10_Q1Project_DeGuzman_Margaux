from browser import document

def create_order(e):
    prod1 = document.getElementById("spirit")
    prod2 = document.getElementById("grappler")
    prod3 = document.getElementById("glider")

    # Calculate subtotal by multiplying checkbox value by its checked status (1 or 0)
    subtotal = (float(prod1.value) * prod1.checked +
                float(prod2.value) * prod2.checked +
                float(prod3.value) * prod3.checked)
    
    tax_rate = 0.12 # 12% VAT
    tax = subtotal * tax_rate
    total = subtotal + tax

    receipt = f"""
    <div class="space-y-1">
        <h3 class="font-bold text-slate-900 mb-2">==== Receipt ====</h3>
        <p>Subtotal: {subtotal:.2f}</p>
        <p>Tax (12%): {tax:.2f}</p>
        <p class="pt-2 border-t border-slate-200 font-bold text-indigo-600">Total: {total:.2f}</p>
    </div>
    """
    document.getElementById("show").innerHTML = receipt

# Bind the calculate button to the create_order function
document["calc_btn"].bind("click", create_order)