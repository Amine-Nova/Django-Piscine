async function change() {
  try {
    const response = await fetch("http://127.0.0.1:8000/random");
    if (response.ok) {
      data = await response.json();
      return data.name
    } else {
      throw new Error("Failed to fetch data");
    }
  } catch (error) {
    console.error("Error:", error);
  }
}


async function getName() {
    newName = await change()
    oldName = document.getElementById("name").innerHTML
    while (newName == oldName) {
        console.log("Same name");
        newName = await change()
    }
    document.getElementById("name").innerHTML = "Hello " + newName
} 

setInterval(getName, 42000);
