document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".trix-button").forEach(button => {
        switch (button.getAttribute("title")) {
            case "Bold":
                button.setAttribute("title", "Жирный");
                button.textContent = "Жирный";
                break;
            case "Italic":
                button.setAttribute("title", "Курсив");
                button.textContent = "Курсив";
                break;
            case "Strikethrough":
                button.setAttribute("title", "Перечёркнутый");
                button.textContent = "Перечёркнутый";
                break;
            case "Link":
                button.setAttribute("title", "Ссылка");
                button.textContent = "Ссылка";
                break;
            case "Heading":
                button.setAttribute("title", "Заголовок");
                button.textContent = "Заголовок";
                break;
            case "Quote":
                button.setAttribute("title", "Цитата");
                button.textContent = "Цитата";
                break;
            case "Code":
                button.setAttribute("title", "Код");
                button.textContent = "Код";
                break;
            case "Bullets":
                button.setAttribute("title", "Список с маркерами");
                button.textContent = "Список с маркерами";
                break;
            case "Numbers":
                button.setAttribute("title", "Нумерованный список");
                button.textContent = "Нумерованный список";
                break;
            case "Decrease Level":
                button.setAttribute("title", "Уменьшить уровень");
                button.textContent = "Уменьшить уровень";
                break;
            case "Increase Level":
                button.setAttribute("title", "Увеличить уровень");
                button.textContent = "Увеличить уровень";
                break;
            case "Attach Files":
                button.setAttribute("title", "Прикрепить файлы");
                button.textContent = "Прикрепить файлы";
                break;
            case "Undo":
                button.setAttribute("title", "Отменить");
                button.textContent = "Отменить";
                break;
            case "Redo":
                button.setAttribute("title", "Повторить");
                button.textContent = "Повторить";
                break;
            
        }
    });
});


document.addEventListener("DOMContentLoaded", () => {
    const editor = document.querySelector("trix-editor");
    const placeholder = document.querySelector(".trix-placeholder");

    function updatePlaceholderVisibility() {
        if (editor.editor.getDocument().toString().trim() === "") {
            placeholder.style.opacity = "1";
        } else {
            placeholder.style.opacity = "0";
        }
    }

    updatePlaceholderVisibility()

    editor.addEventListener("trix-change", updatePlaceholderVisibility);

    editor.addEventListener("focus", () => {
        placeholder.style.opacity = "0";
    });

    editor.addEventListener("blur", () => {
        updatePlaceholderVisibility();
    });
});
