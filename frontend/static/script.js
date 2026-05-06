const form = document.getElementById("calcForm");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(form);

    const res = await fetch("/calculate", {
        method: "POST",
        body: formData
    });

    const data = await res.json();

    document.getElementById("result").innerHTML = `
        <h3>Result: ${data.result} ${data.unit}</h3>
        <pre>${data.breakdown}</pre>
    `;
});

async function loadRecords() {
    const res = await fetch("/records");
    const data = await res.json();

    let table = "<tr><th>User</th><th>Image Size</th><th>Real Size</th></tr>";

    data.forEach(r => {
        table += `<tr>
            <td>${r.username}</td>
            <td>${r.image_size}</td>
            <td>${r.real_size} ${r.unit}</td>
        </tr>`;
    });

    document.getElementById("recordsTable").innerHTML = table;
}

async function deleteRecords() {
    await fetch("/delete_all", { method: "DELETE" });
    alert("Records deleted");
}