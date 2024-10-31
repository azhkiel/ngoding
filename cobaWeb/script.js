function appendToDisplay(value) {
    document.getElementById("display").value += value;
  }
  
  function clearDisplay() {
    document.getElementById("display").value = "";
  }
  
  function calculate() {
    let expression = document.getElementById("display").value;
    let result;
  
    try {
      result = eval(expression);
      if (result === Infinity || isNaN(result)) {
        throw new Error("Invalid operation");
      }
    } catch (error) {
      result = "Error";
    }
  
    document.getElementById("display").value = result;
    }
