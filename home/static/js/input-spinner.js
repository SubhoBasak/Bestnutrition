
function inputChangeHandler() {
    let temp = parseInt(document.getElementById('product-qt').value)
    if (temp == 0)
        document.getElementById('product-qt').value = 1
    else if (temp < 1)
        document.getElementById('product-qt').value = temp * -1
    else
        document.getElementById('product-qt').value = temp

}

function prepend() {
    let temp = parseInt(document.getElementById('product-qt').value)
    if (temp <= 1)
        return
    document.getElementById('product-qt').value = temp - 1
}

function append() {
    let temp = parseInt(document.getElementById('product-qt').value)
    document.getElementById('product-qt').value = temp + 1
}