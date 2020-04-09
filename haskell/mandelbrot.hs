import Graphics.GL.Types
import Graphics.UI.GLUT

allComplex :: [(GLfloat,GLfloat)]
allComplex = [ (i, j) | i <- [-1.5, -1.498..1], j <- [-1, -0.998..1] ]


zadd (a1, b1) (a2, b2) = ((a1 + a2), (b1 + b2))
zmult (a1, b1) (a2, b2) = ((a1*a2 - b1*b2), (a1*b2 + a2*b1))
zsquare z = zmult z z

zdist (a, b) = sqrt (a*a + b*b)

mandelbrot c 0 = (0, 0)
mandelbrot c n = zadd (zsquare (mandelbrot c (n-1))) c

isMandelUnderT t z n = (zdist (mandelbrot z n)) < t

filteredComplex = filter (\z -> isMandelUnderT 10 z 30) allComplex

complexToPoint (a, b) = (a, b, 0)
myPoints = map complexToPoint filteredComplex

main :: IO ()
main = do
  (_progName, _args) <- getArgsAndInitialize
  _window <- createWindow "Hello World"
  displayCallback $= display
  mainLoop

display :: DisplayCallback
display = do
  clear [ ColorBuffer ]
  renderPrimitive Points $
    mapM_ (\(x, y, z) -> vertex $ Vertex3 (x + 0.5) y z) myPoints
  flush
