async function predictScore() {
    const hours = document.getElementById("hours").value;
    const response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ hours: parseFloat(hours) })
    });
    const data = await response.json();
    document.getElementById("result").innerText = 
        `Predicted Score: ${data.predicted_score}`;
}
