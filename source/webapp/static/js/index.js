

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

    let first = parseInt(document.getElementById("first").value) ;
    let second = parseInt(document.getElementById("second").value) ;

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
    console.log(requestBody)


    let response = await fetch(url, requestBody);
    let data =  await response.json();

    console.log(data.answer);

    let answerPlace = document.getElementById("div_response")
    if (data.answer === "Need to input two numbers"){
        answerPlace.style.color = "red";
    }
    else if(data.answer === "Zero division error"){
        answerPlace.style.color = "red"
    }else{
        answerPlace.style.color = "green"
    }
    answerPlace.innerText = data.answer
}
