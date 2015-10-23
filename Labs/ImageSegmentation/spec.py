# name this file solutions.py
"""Volume I Lab : 
<Name>
<Class>
<Date>
"""

# Helper function for computing the adjacency matrix of an image
def getNeighbors(index, radius, height, width):
    '''
    Calculate the indices and distances of pixels within radius
    of the pixel at index, where the pixels are in a (height, width) shaped
    array. The returned indices are with respect to the flattened version of the
    array. This is a helper function for adjacency.
    
    Inputs:
        index (int): denotes the index in the flattened array of the pixel we are 
                looking at
        radius (float): radius of the circular region centered at pixel (row, col)
        height, width (int,int): the height and width of the original image, in pixels
    Returns:
        indices (int): a flat array of indices of pixels that are within distance r
                   of the pixel at (row, col)
        distances (int): a flat array giving the respective distances from these 
                     pixels to the center pixel.
    '''
    # Find appropriate row, column in unflattened image for flattened index
    row, col = index/width, index%width
    # Cast radius to an int (so we can use arange)
    r = int(radius)
    # Make a square grid of side length 2*r centered at index
    # (This is the sup-norm)
    x = np.arange(max(col - r, 0), min(col + r+1, width))
    y = np.arange(max(row - r, 0), min(row + r+1, height))
    X, Y = np.meshgrid(x, y)
    # Narrows down the desired indices using Euclidean norm
    # (i.e. cutting off corners of square to make circle)
    R = np.sqrt(((X-np.float(col))**2+(Y-np.float(row))**2))
    mask = (R<radius)
    # Return the indices of flattened array and corresponding distances
    return (X[mask] + Y[mask]*width, R[mask])

# Helper function used for testing connectivity in problem 2.
def sparse_generator(n, c):
    ''' Return a symmetric nxn matrix with sparsity determined by c.
    Inputs:
        n (int): dimension of matrix
        c (float): a float in [0,1]. Larger values of c will produce
            matrices with more entries equal to zero.
    Returns:
        sparseMatrix (array): a matrix defined according the n and c
    '''
    A = np.random.rand(n**2).reshape((n, n))
    A = ( A > c**(.5) )
    return A.T.dot(A)

# Helper function used to display the images.
def displayPosNeg(img,pos,neg):
    '''
    Displays the original image along with the positive and negative
    segments of the image.
    
    Inputs:
        img (array): Original image
        pos (array): Positive segment of the original image
        neg (array): Negative segment of the original image
    Returns:
        Plots the original image along with the positive and negative
            segmentations.
    '''
    plt.subplot(131)
    plt.imshow(neg)
    plt.subplot(132)
    plt.imshow(pos)
    plt.subplot(133)
    plt.imshow(img)
    plt.show()

# Helper function used to convert the image into the correct format.
def getImage(filename='dream.png'):
    '''
    Reads an image and converts the image to a 2-D array of brightness
    values (or grayscale).
    
    Inputs:
        filename (str): filename of the image to be transformed.
    '''
    img_color = plt.imread(filename)
    return (img_color[:,:,0]+img_color[:,:,1]+img_color[:,:,2])/3.0


# Problem 1: Implement this function.
def laplacian(A):
    '''
    Compute the Laplacian matrix of the adjacency matrix A.
    Inputs:
        A (array): adjacency matrix for undirected weighted graph,
             shape (n,n)
    Returns:
        L (array): Laplacian matrix of A
        
    '''
    raise NotImplementedError("Problem 1 Incomplete")

# Problem 2: Implement this function.
def secondEigenvalue(A):
    '''
    Compute the second smallest eigenvalue of the adjacency matrix A.
    Inputs:
        A (array): adjacency matrix for undirected weighted graph,
             shape (n,n)
    Returns:
        lambda (float): second smallest eigenvalue of L
    '''
    raise NotImplementedError("Problem 2 Incomplete")

# Problem 3: Implement this function.
def adjacency(img, radius = 5.0, sigmaI = .15, sigmaX = 1.7):
    '''
    Compute the weighted adjacency matrix for
    the image array img given radius. Do all computations with sparse matrices.
    Also, return an array giving the main diagonal of the degree matrix.
    
    Inputs:
        img (array): an array representing the image as returned by getImage()
        radius (float): maximum distance where the weight isn't 0
        sigmaI (float): some constant to help define the weight
        sigmaD (float): some constant to help define the weight
    Returns:
        W (sparse array(csc)): the weighted adjacency matrix of img, in sparse form.
        D (array): 1D array representing the main diagonal of the degree matrix.
    '''
    raise NotImplementedError("Problem 3 Incomplete")

# Problem 4: Implement this function.
def segment(img):
    '''
    Compute and return the two segments of the image as described in the text. 
    Compute L, the laplacian matrix. Then compute D^(-1/2)LD^(-1/2),and find
    the eigenvector corresponding to the second smallest eigenvalue.
    Use this eigenvector to calculate a mask that will be usedto extract 
    the segments of the image.
    Inputs:
        img (array): image array of shape (n,n)
    Returns:
        seg1 (array): an array the same size as img, but with 0's
                for each pixel not included in the positive
                segment (which corresponds to the positive
                entries of the computed eigenvector)
        seg2 (array): an array the same size as img, but with 0's
                for each pixel not included in the negative
                segment.
    '''
    raise NotImplementedError("Problem 4 Incomplete")

