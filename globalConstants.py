class GlobalConstants():
    mainURL="http://localhost:8080/swagger-ui/index.html#/"
    ok="200"
    badRequest="400"
    created="201"
    undocumented="500"

    #writingArea
    body=".body-param__text"
    parameters=".parameters-col_description > input"
    

    #category
    addCategory="#operations-categories-controller-addCategory .opblock-summary-control"
    getCategories="#operations-categories-controller-getAll_1 .opblock-summary-control"
    deleteCategories="#operations-categories-controller-deleteAll_1 .opblock-summary-control"
    updateCategory="#operations-categories-controller-updateCategory .opblock-summary-control"
    deleteCategory="#operations-categories-controller-deleteCategory .opblock-summary-path span"
    #product
    getAll = "#operations-products-controller-getAll .opblock-summary-control"
    updateProduct="#operations-products-controller-updateProduct .opblock-summary-control"
    addProduct="#operations-products-controller-addProduct .opblock-summary-control"
    deleteAll="#operations-products-controller-deleteAll .opblock-summary-control"
    getByQueryProductResponse="#operations-products-controller-getByQueryProductResponse .opblock-summary-control"
    getByCategoryProductResponse="#operations-products-controller-getByCategoryProductResponse .opblock-summary-path span"
    deleteProduct="#operations-products-controller-deleteProduct .opblock-summary-path span"
    


    addCategoryExample="{\"name\":\"example\"}"
    addProductExaple="{\"description\":\"example\",\"image\":\"example\",\"price\":9.99,\"title\":\"example\",\"categoryId\":5}"


