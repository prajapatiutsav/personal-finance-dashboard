fetch("/data")
.then(res => res.json())
.then(data => {

const labels = Object.keys(data)
const values = Object.values(data)

new Chart(document.getElementById("barChart"), {

type: "bar",

data: {

labels: labels,

datasets: [{
label: "Expenses",
data: values
}]

}

})

new Chart(document.getElementById("pieChart"), {

type: "pie",

data: {

labels: labels,

datasets: [{
data: values
}]

}

})

})
