document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('div.highlight').forEach((codeBlock) => {
        const copyButton = document.createElement('button');
        copyButton.className = 'copy-button';
        copyButton.textContent = 'Copy';

        Object.assign(copyButton.style, {
            position: 'absolute',
            top: '5px',
            right: '5px',
            padding: '3px 8px',
            border: '1px solid #ccc',
            borderRadius: '4px',
            backgroundColor: '#f0f0f0',
            color: '#333',
            cursor: 'pointer',
            opacity: '0.7',
            transition: 'opacity 0.2s',
            fontSize: '12px',
        });

        codeBlock.style.position = 'relative';
        copyButton.style.opacity = '0';

        codeBlock.addEventListener('mouseover', () => { copyButton.style.opacity = '0.7'; });
        codeBlock.addEventListener('mouseout', () => { copyButton.style.opacity = '0'; });
        copyButton.addEventListener('mouseover', (e) => { e.currentTarget.style.opacity = '1'; });
        copyButton.addEventListener('mouseout', (e) => { e.currentTarget.style.opacity = '0.7'; });


        codeBlock.appendChild(copyButton);

        copyButton.addEventListener('click', (event) => {
            event.stopPropagation();
            const code = codeBlock.querySelector('pre').innerText;

            navigator.clipboard.writeText(code).then(() => {
                copyButton.textContent = 'Copied!';
                copyButton.style.borderColor = 'green';
                setTimeout(() => {
                    copyButton.textContent = 'Copy';
                    copyButton.style.borderColor = '#ccc';
                }, 2000);
            }).catch(err => {
                console.error('Failed to copy text: ', err);
                copyButton.textContent = 'Error';
            });
        });
    });
});
