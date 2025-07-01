let currentTheme = 'light';
let currentCipher = 'fernet';
        
        // DOM elements
        const menuToggle = document.getElementById('menuToggle');
        const sidebar = document.getElementById('sidebar');
        const mainContent = document.getElementById('mainContent');
        const themeToggle = document.getElementById('themeToggle');
        const encryptModal = document.getElementById('encryptModal');
        const closeModal = document.getElementById('closeModal');
        const encryptionForm = document.getElementById('encryptionForm');
        const outputContainer = document.getElementById('outputContainer');
        const copyButton = document.getElementById('copyButton');
        const navLinks = document.querySelectorAll('.nav-link');
        const cardButtons = document.querySelectorAll('.card-button');

        // Initialize
        document.addEventListener('DOMContentLoaded', function() {
            initializeTheme();
            setupEventListeners();
            setupCopyToClipboard();
        });

        function initializeTheme() {
            // Note: Using in-memory storage instead of localStorage
            if (currentTheme === 'dark') {
                document.body.classList.add('dark-mode');
                themeToggle.innerHTML = '<i class="fas fa-sun"></i><span>Light Mode</span>';
            }
        }

        function setupEventListeners() {
            // Menu toggle
            menuToggle.addEventListener('click', function() {
                sidebar.classList.toggle('collapsed');
                mainContent.classList.toggle('expanded');
            });

            // Theme toggle
            themeToggle.addEventListener('click', function() {
                document.body.classList.toggle('dark-mode');
                currentTheme = document.body.classList.contains('dark-mode') ? 'dark' : 'light';
                
                if (currentTheme === 'dark') {
                    themeToggle.innerHTML = '<i class="fas fa-sun"></i><span>Light Mode</span>';
                } else {
                    themeToggle.innerHTML = '<i class="fas fa-moon"></i><span>Dark Mode</span>';
                }
            });

            // Navigation links
            navLinks.forEach(link => {
                link.addEventListener('click', function(e) {
                    e.preventDefault();
                    navLinks.forEach(l => l.classList.remove('active'));
                    this.classList.add('active');
                    currentCipher = this.dataset.cipher;
                });
            });

            // Card buttons
            cardButtons.forEach(button => {
                button.addEventListener('click', function() {
                    currentCipher = this.dataset.cipher;
                    document.getElementById('cipherSelect').value = currentCipher;
                    document.getElementById('modalTitle').textContent = `${currentCipher.toUpperCase()} Encryption`;
                    openModal();
                });
            });

            // Modal events
            closeModal.addEventListener('click', closeModalHandler);
            encryptModal.addEventListener('click', function(e) {
                if (e.target === encryptModal) {
                    closeModalHandler();
                }
            });

            // Form submission
            encryptionForm.addEventListener('submit', handleFormSubmission);

            // Escape key to close modal
            document.addEventListener('keydown', function(e) {
                if (e.key === 'Escape' && encryptModal.classList.contains('show')) {
                    closeModalHandler();
                }
            });
        }

        function openModal() {
            encryptModal.classList.add('show');
            document.body.style.overflow = 'hidden';
        }

        function closeModalHandler() {
            encryptModal.classList.remove('show');
            document.body.style.overflow = '';
        }

        function handleFormSubmission(e) {
            e.preventDefault();
            const text = document.getElementById('plainText').value;
            const cipher = document.getElementById('cipherSelect').value;
            const mode = document.getElementById('modeSelect').value;
            const submitButton = document.getElementById('submitButton');
            
            if (!text.trim()) {
            showOutput('❌ Please enter some text to process.', 'error');
            return;
            }

        submitButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';
        submitButton.classList.add('loading');
        showOutput('⏳ Processing your request...', 'loading');

        const url = mode === 'encrypt' ? '/encrypt' : '/decrypt';

        fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text, cipher }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.result) {
                showOutput(data.result, 'success');
                closeModalHandler();
                encryptionForm.reset();
            } else {
                showOutput(`❌ ${data.error}`, 'error');
            }
        })
        .catch(error => {
            showOutput(`❌ Error: ${error.message}`, 'error');
        })
        .finally(() => {
            submitButton.innerHTML = '<i class="fas fa-play"></i> Process Text';
            submitButton.classList.remove('loading');
        });
}
