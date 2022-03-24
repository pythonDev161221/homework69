
// async function onEchoClick(event){
//     let url = event.target.dataset.
// }
async function onTakeCsrf(event){
    url = event.target.dataset.toCsrf;
    console.log(url);
    let response = fetch(url);
    console.log(response);
    console.log(document.cookie)
    var csrf = document.cookie.split("=")[1]
    console.log(csrf)
    // let responseBody = await response.json()
    // console.log(responseBody)
}
// let response = fetch(url, {method: "POST", X-csrf: body: , });

function takeNumbers(){

    let first = document.getElementById("first").value;
    let second = document.getElementById("second").value;

    return {"A": first, "B": second}
}



async function onAddClick(event){
    let urlC = event.target.dataset.toCsrf;
    let responseC = await fetch(urlC);
    let csrf = document.cookie.split("=")[1];
    let url = event.target.dataset.addUrl;
    let requestBody = {method: "POST"};
    requestBody["headers"] = {"X-CSRFToken": csrf};
    requestBody["headers"]["content-type"] = "application/json"

    content = takeNumbers();

    requestBody["body"] = JSON.stringify(content)
    console.log(requestBody)


    let response = await fetch(url, requestBody);
    let data =  await response.json();

    console.log(data.answer);

    answerPlace = document.getElementById("div_response")
    answerPlace.innerText = data.answer
}

async function onSubtractClick(event){
    let urlC = event.target.dataset.toCsrf;
    let responseC = await fetch(urlC);
    let csrf = document.cookie.split("=")[1];
    console.log(csrf)
    let url = event.target.dataset.addUrl;
    let requestBody = {method: "POST"};
    requestBody["headers"] = {"X-CSRFToken": csrf};
    requestBody["headers"]["content-type"] = "application/json"

    content = takeNumbers();

    requestBody["body"] = JSON.stringify(content)
    console.log(requestBody)


    let response = await fetch(url, requestBody);
    let data =  await response.json();

    console.log(data.answer);

    answerPlace = document.getElementById("div_response")
    answerPlace.innerText = data.answer
}

async function onMultiplyClick(event){
    let urlC = event.target.dataset.toCsrf;
    let responseC = await fetch(urlC);
    let csrf = document.cookie.split("=")[1];
    console.log(csrf)
    let url = event.target.dataset.addUrl;
    let requestBody = {method: "POST"};
    requestBody["headers"] = {"X-CSRFToken": csrf};
    requestBody["headers"]["content-type"] = "application/json"

    content = takeNumbers();

    requestBody["body"] = JSON.stringify(content)
    console.log(requestBody)


    let response = await fetch(url, requestBody);
    let data =  await response.json();

    console.log(data.answer);

    answerPlace = document.getElementById("div_response")
    answerPlace.innerText = data.answer
}