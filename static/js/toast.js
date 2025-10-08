function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    
    if (!toastComponent) return;

    // Remove all type classes first
    toastComponent.classList.remove(
        'bg-[#BE123C]-50', 'border-[#BE123C]-500', 'text-[#BE123C]-600',
        'bg-[#84CC16]-50', 'border-[#84CC16]-500', 'text-[#84CC16]-600',
        'bg-white', 'border-gray-300', 'text-gray-800'
    );

    // Set type styles and icon
    if (type === 'success') {
        toastComponent.classList.add('bg-[#84CC16]-50', 'border-[#84CC16]-500', 'text-[#84CC16]-600');
        toastComponent.style.border = '1px solid #0b4721ff';
    } else if (type === 'error') {
        toastComponent.classList.add('bg-[#BE123C]-50', 'border-[#BE123C]-500', 'text-[#BE123C]-600');
        toastComponent.style.border = '1px solid #f66767ff';
    } else {
        toastComponent.classList.add('bg-white', 'border-gray-300', 'text-gray-800');
        toastComponent.style.border = '1px solid #d1d5db';
    }

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    toastComponent.classList.remove('opacity-0', 'translate-y-64');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-64');
    }, duration);
}