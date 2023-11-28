async function Recommendations() {
    const response = await fetch(`http://127.0.0.1:5000/getRecommendations`);
    const res = await response.json();
    console.log('res', res);
    const rootElement = document.getElementById('root2');
    rootElement.innerHTML = '<h1>Recommendations</h1>'; // Clear previous content

    const resultContainer = document.createElement('div');
    resultContainer.classList.add('result-container');

    res.forEach(product => {
        const productContainer = document.createElement('div');
        productContainer.classList.add('product-card');

        const imageElement = document.createElement('img');
        imageElement.classList.add('product-image');
        imageElement.src = product.images;
        imageElement.alt = product.title;

        const nameElement = document.createElement('p');
        nameElement.classList.add('product-name');
        nameElement.textContent = product.title;

        const websiteElement = document.createElement('p');
        websiteElement.classList.add('product-website');
        websiteElement.textContent = `Website: ${product.website}`;

        const priceElement = document.createElement('p');
        priceElement.classList.add('product-price');
        priceElement.textContent = `Price: ${product.price}`;

        const linkElement = document.createElement('a');
        linkElement.classList.add('product-link');
        linkElement.href = product.link;
        linkElement.textContent = 'View Product';

        productContainer.appendChild(imageElement);
        productContainer.appendChild(nameElement);
        productContainer.appendChild(websiteElement);
        productContainer.appendChild(priceElement);
        productContainer.appendChild(linkElement);

        resultContainer.appendChild(productContainer);
    });

    rootElement.appendChild(resultContainer);
}