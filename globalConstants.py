class GlobalConstants():
    mainURL="http://localhost:8080/swagger-ui/index.html#/"
    ok="200"
    badRequest="400"
    created="201"
    undocumented="500"

    #writingArea
    body=".body-param__text"
    parameters=".parameters-col_description > input"
    
    #controller
    addCategory="#operations-categories-controller-addCategory .opblock-summary-control"
    getCategories="#operations-categories-controller-getAll_1 .opblock-summary-control"
    deleteCategories="#operations-categories-controller-deleteAll_1 .opblock-summary-control"
    updateCategory="#operations-categories-controller-updateCategory .opblock-summary-control"
    deleteCategory="#operations-categories-controller-deleteCategory .opblock-summary-path span"
    
    


    addCategoryExample="{\"name\":\"example\"}"
