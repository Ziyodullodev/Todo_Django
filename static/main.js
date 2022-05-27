const form = document.querySelector('#new-task-form');
const input = document.querySelector('#new-task-input');
const list_el = document.querySelector('#tasks');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    const task = input.value;
    if (task) {
        const task_el = document.createElement('div');
        task_el.classList.add('task');

        const task_content_el = document.createElement('div');
        task_content_el.classList.add('content');

        const task__input = document.createElement('input');
        task__input.type = "text";
        task__input.classList.add("text");
        task__input.value = task;
        task__input.setAttribute('readonly', false);
        task_content_el.appendChild(task__input);

        const task__btn_content = document.createElement("div");
        task__btn_content.classList.add("actions");

        const task__btn_edit = document.createElement("button");
        task__btn_edit.classList.add("edit");
        task__btn_edit.textContent = "Edit";
        task__btn_edit.setAttribute('onclick', "edit__task(this)");
        task__btn_content.appendChild(task__btn_edit);

        const task__btn_delete = document.createElement("button");
        task__btn_delete.classList.add("delete");
        task__btn_delete.textContent = "Delete";
        task__btn_delete.setAttribute('onclick', "delete__task(this)");
        task__btn_content.appendChild(task__btn_delete);

        list_el.appendChild(task_el);
        task_el.appendChild(task_content_el);
        task_el.appendChild(task__btn_content);

        input.value = "";
    }
});

function delete__task(e) {
    e.parentElement.parentElement.remove();
}

function edit__task(e) {
    if (e) {
        let a = e.parentElement.previousElementSibling.childNodes[0].value + " ";
        e.parentElement.previousElementSibling.childNodes[0].removeAttribute('readonly');
        e.parentElement.previousElementSibling.childNodes[0].value = a;
        e.parentElement.previousElementSibling.childNodes[0].focus();

        function addMultipleListeners(element, events, handler, useCapture) {
            let handlerFn = function (e) {
                handler(e);
            }
            for (let i = 0; i < events.length; i += 1) {
                element.addEventListener(events[i], handlerFn, useCapture);
            }
        }
        
        function handler(er) {
            if(er?.which === 13 || !er.cancelable) {
                e.parentElement.previousElementSibling.childNodes[0].setAttribute('readonly', false);
            }
        };
        
        addMultipleListeners(
            e.parentElement.previousElementSibling.childNodes[0],
            ['keyup', 'focusout'],
            handler,
            false);
    }

}


