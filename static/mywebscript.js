// const runSentimentAnalysis = async () => {
//     const textToAnalyze = document.getElementById("textToAnalyze").value;

//     try {
//         const response = await fetch(`emotionDetector?textToAnalyze=${textToAnalyze}`);
        
//         if (!response.ok) {
//             throw new Error(`HTTP error! Status: ${response.status}`);
//         }

//         const result = await response.text();
//         document.getElementById("system_response").innerHTML = result;
//     } catch (error) {
//         console.error("Error during sentiment analysis:", error.message);
//         // Handle the error, e.g., display a user-friendly message to the user
//     }
// };

// // Example of calling the function when a button is clicked
// document.getElementById("analyzeButton").addEventListener("click", runSentimentAnalysis);


let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze"+"="+textToAnalyze, true);
    xhttp.send();
}
