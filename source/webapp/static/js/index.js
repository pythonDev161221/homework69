

// async function onTakeCsrf(event){
//     let url = event.target.dataset.toCsrf;
//     console.log(url);
//     let response = fetch(url);
//     console.log(response);
//     console.log(document.cookie)
//     var csrf = document.cookie.split("=")[1]
//     console.log(csrf)
// }


function takeNumbers(){

    let first = document.getElementById("first").value;
    let second = document.getElementById("second").value ;

    return {"A": first, "B": second}
}



async function onAddClick(event){
    let urlC = event.target.dataset.toCsrf;
    await fetch(urlC);
    let csrf = document.cookie.split("=")[1];
    let url = event.target.dataset.addUrl;
    let requestBody = {method: "POST"};
    requestBody["headers"] = {"X-CSRFToken": csrf};
    requestBody["headers"]["content-type"] = "application/json"

    content = takeNumbers();

    requestBody["body"] = JSON.stringify(content)

    let response = await fetch(url, requestBody);
    let answerPlace = document.getElementById("div_response")
    console.log(response.ok)
    if (response.ok) {
        let data = await response.json();
        answerPlace.style.color = "green"
        answerPlace.innerText = data.answer
    } else {
        let data = await response.json();
        console.log(data)
        answerPlace.style.color = "red"
        answerPlace.innerText = data.error
    }
}
