function answer_index_finder( answer_id, result, hiddenField) {
    let text = document.getElementById("passage").textContent;
    let answer = document.getElementById(answer_id).value;
    let index = text.indexOf(answer);
    console.log(answer); 
    console.log(index);
    document.querySelector(result).innerHTML = index;
    document.getElementById(hiddenField).value = index;
}

