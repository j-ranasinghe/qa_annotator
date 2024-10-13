let allData = [];
let currentIndex = 101;
 

// Function to display the data
function displayData(data) {
    document.getElementById('title').innerText = data.title;;
    document.getElementById('id').innerText = data.id;
    document.getElementById('passage').innerText = data.context;
    document.getElementById('index').innerText = data.index;
}

// Load one entry at a time when the button is clicked
function loadNextEntry() {
    if (currentIndex < allData.length) {
        displayData(allData[currentIndex]);
        currentIndex++;  // Increment the index for the next load
    } else {
        alert('No more data to load.');
    }
}

// Submit form data
async function submitForm() {
    const title = document.getElementById('title').innerText;
    const id = document.getElementById('id').innerText;
    const context = document.getElementById('passage').innerText;

    const question = document.getElementById('question').value;
    const answer_1 = document.getElementById('answer-1').value;
    const answer_start_1 = document.getElementById('start-point-answer-1').value;

    const question_2 = document.getElementById('question_2').value;
    const answer_2 = document.getElementById('answer-2').value;
    const answer_start_2 = document.getElementById('start-point-answer-2').value;
    console.log(answer_start_2);
    console.log(question_2);

    const id_2 = id + "_2"
    console.log(id_2);
    
    // const answer_3 = document.getElementById('answer-3').value;
    // const answer_start_3 = document.getElementById('start-point-answer-3').value;


    const response = await fetch('/submit', { 
        method: 'POST',
        headers: { 
            'Content-Type': 'application/json; charset=UTF-8',
        }, 
            body: JSON.stringify( {
                title: title,
                paragraphs: [{
                context: context,
                qas: [{
                    answers: [{
                        text: answer_1,
                        answer_start: answer_start_1,
                    }],
                    question: question,
                    id: id,  
                },{
                    answers: [{
                        text: answer_2,
                        answer_start: answer_start_2,
                    }],
                    question: question_2,
                    id: id_2,
                }
                    
                ]
            }]
        
            }),
    });

    const result = await response.json();
    alert(result.message);
}

// Initial setup: This is used to load the data passed from Flask
function initializeData(flaskData) {
    allData = flaskData; 
    console.log(allData);
}

// Function to get the answer starting point index
function answer_index_finder( answer_id, result, hiddenField) {
    let text = document.getElementById("passage").textContent;
    let answer = document.getElementById(answer_id).value;
    let index = text.indexOf(answer);
    document.querySelector(result).innerHTML = index;
    document.getElementById(hiddenField).value = index;
}