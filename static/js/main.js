document.getElementById('searchForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const query = document.getElementById('searchQuery').value;
    const tool = document.getElementById('searchTool').value;
    const resultsContainer = document.getElementById('results');
    
    if (!query.trim()) return;
    
    // Show loading state
    resultsContainer.innerHTML = '<p>Searching...</p>';
    
    try {
        const response = await fetch('/api/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query, tool }),
        });
        
        const data = await response.json();
        
        // Display results
        resultsContainer.innerHTML = `
            <h2>Results for ${tool.toUpperCase()}</h2>
            <pre>${JSON.stringify(data.results, null, 2)}</pre>
        `;
    } catch (error) {
        resultsContainer.innerHTML = `<p class="error">Error: ${error.message}</p>`;
    }
});