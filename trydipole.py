
OpenDatabase("localhost:./tagpluto000000.vtk", 0)
DefineVectorExpression("b", "{b1,b2,b3}")

AddPlot("Contour", "den", 1, 1)
AddPlot("Streamline", "b", 1, 1)


# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.983693, -0.178169, -0.0245633)
View3DAtts.focus = (99.5, 99.5, 99.5)
View3DAtts.viewUp = (-0.0310104, 0.0334909, 0.998958)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 172.339
View3DAtts.nearPlane = -344.678
View3DAtts.farPlane = 344.678
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (99.5, 99.5, 99.5)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

SetActivePlots((0, 1))
AddOperator("Box", 1)
BoxAtts = BoxAttributes()
BoxAtts.amount = BoxAtts.Some  # Some, All
BoxAtts.minx = 100
BoxAtts.maxx = 400
BoxAtts.miny = 100
BoxAtts.maxy = 400
BoxAtts.minz = 100
BoxAtts.maxz = 400
BoxAtts.inverse = 0
SetOperatorOptions(BoxAtts, 1)

StreamlineAtts = StreamlineAttributes()
StreamlineAtts.sourceType = StreamlineAtts.SpecifiedBox  # SpecifiedPoint, SpecifiedPointList, SpecifiedLine, SpecifiedCircle, SpecifiedPlane, SpecifiedSphere, SpecifiedBox, Selection
StreamlineAtts.pointSource = (0, 0, 0)
StreamlineAtts.lineStart = (0, 0, 0)
StreamlineAtts.lineEnd = (1, 0, 0)
StreamlineAtts.planeOrigin = (0, 0, 0)
StreamlineAtts.planeNormal = (0, 0, 1)
StreamlineAtts.planeUpAxis = (0, 1, 0)
StreamlineAtts.radius = 1
StreamlineAtts.sphereOrigin = (0, 0, 0)
StreamlineAtts.boxExtents = (0, 1, 0, 1, 0, 1)
StreamlineAtts.useWholeBox = 1
StreamlineAtts.pointList = (0, 0, 0, 1, 0, 0, 0, 1, 0)
StreamlineAtts.sampleDensity0 = 4
StreamlineAtts.sampleDensity1 = 4
StreamlineAtts.sampleDensity2 = 4
StreamlineAtts.coloringMethod = StreamlineAtts.Solid  # Solid, ColorBySpeed, ColorByVorticity, ColorByLength, ColorByTime, ColorBySeedPointID, ColorByVariable, ColorByCorrelationDistance
StreamlineAtts.colorTableName = "Default"
StreamlineAtts.singleColor = (255, 255, 255, 255)
StreamlineAtts.legendFlag = 1
StreamlineAtts.lightingFlag = 1
StreamlineAtts.integrationDirection = StreamlineAtts.Both  # Forward, Backward, Both
StreamlineAtts.maxSteps = 1000
StreamlineAtts.terminateByDistance = 0
StreamlineAtts.termDistance = 10
StreamlineAtts.terminateByTime = 0
StreamlineAtts.termTime = 10
StreamlineAtts.maxStepLength = 0.1
StreamlineAtts.limitMaximumTimestep = 0
StreamlineAtts.maxTimeStep = 0.1
StreamlineAtts.relTol = 0.00001
StreamlineAtts.absTolSizeType = StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
StreamlineAtts.absTolAbsolute = 1e-06
StreamlineAtts.absTolBBox = 1e-06
StreamlineAtts.fieldType = StreamlineAtts.Default  # Default, FlashField, M3DC12DField, M3DC13DField, Nek5000Field, NIMRODField
StreamlineAtts.fieldConstant = 1
StreamlineAtts.velocitySource = (0, 0, 0)
StreamlineAtts.integrationType = StreamlineAtts.DormandPrince  # Euler, Leapfrog, DormandPrince, AdamsBashforth, RK4, M3DC12DIntegrator
StreamlineAtts.parallelizationAlgorithmType = StreamlineAtts.VisItSelects  # LoadOnDemand, ParallelStaticDomains, MasterSlave, VisItSelects
StreamlineAtts.maxProcessCount = 10
StreamlineAtts.maxDomainCacheSize = 3
StreamlineAtts.workGroupSize = 32
StreamlineAtts.pathlines = 0
StreamlineAtts.pathlinesOverrideStartingTimeFlag = 0
StreamlineAtts.pathlinesOverrideStartingTime = 0
StreamlineAtts.pathlinesPeriod = 0
StreamlineAtts.pathlinesCMFE = StreamlineAtts.POS_CMFE  # CONN_CMFE, POS_CMFE
StreamlineAtts.coordinateSystem = StreamlineAtts.AsIs  # AsIs, CylindricalToCartesian, CartesianToCylindrical
StreamlineAtts.phiScalingFlag = 0
StreamlineAtts.phiScaling = 1
StreamlineAtts.coloringVariable = ""
StreamlineAtts.legendMinFlag = 0
StreamlineAtts.legendMaxFlag = 0
StreamlineAtts.legendMin = 0
StreamlineAtts.legendMax = 1
StreamlineAtts.displayBegin = 0
StreamlineAtts.displayEnd = 1
StreamlineAtts.displayBeginFlag = 0
StreamlineAtts.displayEndFlag = 0
StreamlineAtts.referenceTypeForDisplay = StreamlineAtts.Distance  # Distance, Time, Step
StreamlineAtts.displayMethod = StreamlineAtts.Lines  # Lines, Tubes, Ribbons
StreamlineAtts.tubeSizeType = StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
StreamlineAtts.tubeRadiusAbsolute = 0.125
StreamlineAtts.tubeRadiusBBox = 0.005
StreamlineAtts.ribbonWidthSizeType = StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
StreamlineAtts.ribbonWidthAbsolute = 0.125
StreamlineAtts.ribbonWidthBBox = 0.01
StreamlineAtts.lineWidth = 2
StreamlineAtts.showSeeds = 0
StreamlineAtts.seedRadiusSizeType = StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
StreamlineAtts.seedRadiusAbsolute = 1
StreamlineAtts.seedRadiusBBox = 0.015
StreamlineAtts.showHeads = 0
StreamlineAtts.headDisplayType = StreamlineAtts.Sphere  # Sphere, Cone
StreamlineAtts.headRadiusSizeType = StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
StreamlineAtts.headRadiusAbsolute = 0.25
StreamlineAtts.headRadiusBBox = 0.02
StreamlineAtts.headHeightRatio = 2
StreamlineAtts.opacityType = StreamlineAtts.FullyOpaque  # FullyOpaque, Constant, Ramp, VariableRange
StreamlineAtts.opacityVariable = ""
StreamlineAtts.opacity = 1
StreamlineAtts.opacityVarMin = 0
StreamlineAtts.opacityVarMax = 1
StreamlineAtts.opacityVarMinFlag = 0
StreamlineAtts.opacityVarMaxFlag = 0
StreamlineAtts.tubeDisplayDensity = 10
StreamlineAtts.geomDisplayQuality = StreamlineAtts.Medium  # Low, Medium, High, Super
StreamlineAtts.sampleDistance0 = 10
StreamlineAtts.sampleDistance1 = 10
StreamlineAtts.sampleDistance2 = 10
StreamlineAtts.fillInterior = 1
StreamlineAtts.randomSamples = 0
StreamlineAtts.randomSeed = 0
StreamlineAtts.numberOfRandomSamples = 27
StreamlineAtts.forceNodeCenteredData = 0
StreamlineAtts.issueTerminationWarnings = 1
StreamlineAtts.issueStiffnessWarnings = 1
StreamlineAtts.issueCriticalPointsWarnings = 1
StreamlineAtts.criticalPointThreshold = 0.001
StreamlineAtts.varyTubeRadius = StreamlineAtts.None  # None, Scalar
StreamlineAtts.varyTubeRadiusFactor = 10
StreamlineAtts.varyTubeRadiusVariable = ""
StreamlineAtts.correlationDistanceAngTol = 5
StreamlineAtts.correlationDistanceMinDistAbsolute = 1
StreamlineAtts.correlationDistanceMinDistBBox = 0.005
StreamlineAtts.correlationDistanceMinDistType = StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
StreamlineAtts.selection = ""
SetPlotOptions(StreamlineAtts)


ContourAtts = ContourAttributes()
ContourAtts.defaultPalette.GetControlPoints(0).colors = (255, 0, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(0).position = 0
ContourAtts.defaultPalette.GetControlPoints(1).colors = (0, 255, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(1).position = 0.034
ContourAtts.defaultPalette.GetControlPoints(2).colors = (0, 0, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(2).position = 0.069
ContourAtts.defaultPalette.GetControlPoints(3).colors = (0, 255, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(3).position = 0.103
ContourAtts.defaultPalette.GetControlPoints(4).colors = (255, 0, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(4).position = 0.138
ContourAtts.defaultPalette.GetControlPoints(5).colors = (255, 255, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(5).position = 0.172
ContourAtts.defaultPalette.GetControlPoints(6).colors = (255, 135, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(6).position = 0.207
ContourAtts.defaultPalette.GetControlPoints(7).colors = (255, 0, 135, 255)
ContourAtts.defaultPalette.GetControlPoints(7).position = 0.241
ContourAtts.defaultPalette.GetControlPoints(8).colors = (168, 168, 168, 255)
ContourAtts.defaultPalette.GetControlPoints(8).position = 0.276
ContourAtts.defaultPalette.GetControlPoints(9).colors = (255, 68, 68, 255)
ContourAtts.defaultPalette.GetControlPoints(9).position = 0.31
ContourAtts.defaultPalette.GetControlPoints(10).colors = (99, 255, 99, 255)
ContourAtts.defaultPalette.GetControlPoints(10).position = 0.345
ContourAtts.defaultPalette.GetControlPoints(11).colors = (99, 99, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(11).position = 0.379
ContourAtts.defaultPalette.GetControlPoints(12).colors = (40, 165, 165, 255)
ContourAtts.defaultPalette.GetControlPoints(12).position = 0.414
ContourAtts.defaultPalette.GetControlPoints(13).colors = (255, 99, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(13).position = 0.448
ContourAtts.defaultPalette.GetControlPoints(14).colors = (255, 255, 99, 255)
ContourAtts.defaultPalette.GetControlPoints(14).position = 0.483
ContourAtts.defaultPalette.GetControlPoints(15).colors = (255, 170, 99, 255)
ContourAtts.defaultPalette.GetControlPoints(15).position = 0.517
ContourAtts.defaultPalette.GetControlPoints(16).colors = (170, 79, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(16).position = 0.552
ContourAtts.defaultPalette.GetControlPoints(17).colors = (150, 0, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(17).position = 0.586
ContourAtts.defaultPalette.GetControlPoints(18).colors = (0, 150, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(18).position = 0.621
ContourAtts.defaultPalette.GetControlPoints(19).colors = (0, 0, 150, 255)
ContourAtts.defaultPalette.GetControlPoints(19).position = 0.655
ContourAtts.defaultPalette.GetControlPoints(20).colors = (0, 109, 109, 255)
ContourAtts.defaultPalette.GetControlPoints(20).position = 0.69
ContourAtts.defaultPalette.GetControlPoints(21).colors = (150, 0, 150, 255)
ContourAtts.defaultPalette.GetControlPoints(21).position = 0.724
ContourAtts.defaultPalette.GetControlPoints(22).colors = (150, 150, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(22).position = 0.759
ContourAtts.defaultPalette.GetControlPoints(23).colors = (150, 84, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(23).position = 0.793
ContourAtts.defaultPalette.GetControlPoints(24).colors = (160, 0, 79, 255)
ContourAtts.defaultPalette.GetControlPoints(24).position = 0.828
ContourAtts.defaultPalette.GetControlPoints(25).colors = (255, 104, 28, 255)
ContourAtts.defaultPalette.GetControlPoints(25).position = 0.862
ContourAtts.defaultPalette.GetControlPoints(26).colors = (0, 170, 81, 255)
ContourAtts.defaultPalette.GetControlPoints(26).position = 0.897
ContourAtts.defaultPalette.GetControlPoints(27).colors = (68, 255, 124, 255)
ContourAtts.defaultPalette.GetControlPoints(27).position = 0.931
ContourAtts.defaultPalette.GetControlPoints(28).colors = (0, 130, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(28).position = 0.966
ContourAtts.defaultPalette.GetControlPoints(29).colors = (130, 0, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(29).position = 1
ContourAtts.defaultPalette.smoothing = ContourAtts.defaultPalette.None  # None, Linear, CubicSpline
ContourAtts.defaultPalette.equalSpacingFlag = 1
ContourAtts.defaultPalette.discreteFlag = 1
ContourAtts.defaultPalette.categoryName = "Standard"
ContourAtts.changedColors = (0)
ContourAtts.colorType = ContourAtts.ColorByMultipleColors  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
ContourAtts.colorTableName = "Default"
ContourAtts.invertColorTable = 0
ContourAtts.legendFlag = 1
ContourAtts.lineStyle = ContourAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
ContourAtts.lineWidth = 0
ContourAtts.singleColor = (255, 0, 0, 255)
ContourAtts.SetMultiColor(0, (255, 0, 0, 89))
ContourAtts.SetMultiColor(1, (0, 255, 0, 255))
ContourAtts.SetMultiColor(2, (0, 0, 255, 255))
ContourAtts.SetMultiColor(3, (0, 255, 255, 255))
ContourAtts.SetMultiColor(4, (255, 0, 255, 255))
ContourAtts.SetMultiColor(5, (255, 255, 0, 255))
ContourAtts.SetMultiColor(6, (255, 135, 0, 255))
ContourAtts.SetMultiColor(7, (255, 0, 135, 255))
ContourAtts.SetMultiColor(8, (168, 168, 168, 255))
ContourAtts.SetMultiColor(9, (255, 68, 68, 255))
ContourAtts.contourNLevels = 2
ContourAtts.contourValue = (0.40, 0.48, 0.7, 0.9)
ContourAtts.contourPercent = ()
ContourAtts.contourMethod = ContourAtts.Value  # Level, Value, Percent
ContourAtts.minFlag = 0
ContourAtts.maxFlag = 0
ContourAtts.min = 0
ContourAtts.max = 1
ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
ContourAtts.wireframe = 0
SetPlotOptions(ContourAtts)



AnnotationAtts = AnnotationAttributes()
AnnotationAtts.axes2D.visible = 1
AnnotationAtts.axes2D.autoSetTicks = 1
AnnotationAtts.axes2D.autoSetScaling = 1
AnnotationAtts.axes2D.lineWidth = 0
AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
AnnotationAtts.axes2D.xAxis.title.visible = 1
AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.title.font.scale = 1
AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.title.font.bold = 1
AnnotationAtts.axes2D.xAxis.title.font.italic = 1
AnnotationAtts.axes2D.xAxis.title.userTitle = 0
AnnotationAtts.axes2D.xAxis.title.userUnits = 0
AnnotationAtts.axes2D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes2D.xAxis.title.units = ""
AnnotationAtts.axes2D.xAxis.label.visible = 1
AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.label.font.scale = 1
AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.label.font.bold = 1
AnnotationAtts.axes2D.xAxis.label.font.italic = 1
AnnotationAtts.axes2D.xAxis.label.scaling = 0
AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.xAxis.grid = 0
AnnotationAtts.axes2D.yAxis.title.visible = 1
AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.title.font.scale = 1
AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.title.font.bold = 1
AnnotationAtts.axes2D.yAxis.title.font.italic = 1
AnnotationAtts.axes2D.yAxis.title.userTitle = 0
AnnotationAtts.axes2D.yAxis.title.userUnits = 0
AnnotationAtts.axes2D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes2D.yAxis.title.units = ""
AnnotationAtts.axes2D.yAxis.label.visible = 1
AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.label.font.scale = 1
AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.label.font.bold = 1
AnnotationAtts.axes2D.yAxis.label.font.italic = 1
AnnotationAtts.axes2D.yAxis.label.scaling = 0
AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.yAxis.grid = 0
AnnotationAtts.axes3D.visible = 1
AnnotationAtts.axes3D.autoSetTicks = 1
AnnotationAtts.axes3D.autoSetScaling = 1
AnnotationAtts.axes3D.lineWidth = 0
AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
AnnotationAtts.axes3D.triadFlag = 1
AnnotationAtts.axes3D.bboxFlag = 1
AnnotationAtts.axes3D.xAxis.title.visible = 1
AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.title.font.scale = 1
AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.title.font.bold = 0
AnnotationAtts.axes3D.xAxis.title.font.italic = 0
AnnotationAtts.axes3D.xAxis.title.userTitle = 0
AnnotationAtts.axes3D.xAxis.title.userUnits = 0
AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes3D.xAxis.title.units = ""
AnnotationAtts.axes3D.xAxis.label.visible = 1
AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.label.font.scale = 1
AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.label.font.bold = 0
AnnotationAtts.axes3D.xAxis.label.font.italic = 0
AnnotationAtts.axes3D.xAxis.label.scaling = 0
AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.xAxis.grid = 0
AnnotationAtts.axes3D.yAxis.title.visible = 1
AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.title.font.scale = 1
AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.title.font.bold = 0
AnnotationAtts.axes3D.yAxis.title.font.italic = 0
AnnotationAtts.axes3D.yAxis.title.userTitle = 0
AnnotationAtts.axes3D.yAxis.title.userUnits = 0
AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes3D.yAxis.title.units = ""
AnnotationAtts.axes3D.yAxis.label.visible = 1
AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.label.font.scale = 1
AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.label.font.bold = 0
AnnotationAtts.axes3D.yAxis.label.font.italic = 0
AnnotationAtts.axes3D.yAxis.label.scaling = 0
AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.yAxis.grid = 0
AnnotationAtts.axes3D.zAxis.title.visible = 1
AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.title.font.scale = 1
AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.title.font.bold = 0
AnnotationAtts.axes3D.zAxis.title.font.italic = 0
AnnotationAtts.axes3D.zAxis.title.userTitle = 0
AnnotationAtts.axes3D.zAxis.title.userUnits = 0
AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
AnnotationAtts.axes3D.zAxis.title.units = ""
AnnotationAtts.axes3D.zAxis.label.visible = 1
AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.label.font.scale = 1
AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.label.font.bold = 0
AnnotationAtts.axes3D.zAxis.label.font.italic = 0
AnnotationAtts.axes3D.zAxis.label.scaling = 0
AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.zAxis.grid = 0
AnnotationAtts.axes3D.setBBoxLocation = 0
AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
AnnotationAtts.userInfoFlag = 1
AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.userInfoFont.scale = 1
AnnotationAtts.userInfoFont.useForegroundColor = 1
AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.userInfoFont.bold = 0
AnnotationAtts.userInfoFont.italic = 0
AnnotationAtts.databaseInfoFlag = 1
AnnotationAtts.timeInfoFlag = 1
AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.databaseInfoFont.scale = 1
AnnotationAtts.databaseInfoFont.useForegroundColor = 1
AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.databaseInfoFont.bold = 0
AnnotationAtts.databaseInfoFont.italic = 0
AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
AnnotationAtts.databaseInfoTimeScale = 1
AnnotationAtts.databaseInfoTimeOffset = 0
AnnotationAtts.legendInfoFlag = 1
AnnotationAtts.backgroundColor = (0, 0, 0, 255)
AnnotationAtts.foregroundColor = (255, 255, 255, 255)
AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
AnnotationAtts.backgroundImage = ""
AnnotationAtts.imageRepeatX = 1
AnnotationAtts.imageRepeatY = 1
AnnotationAtts.axesArray.visible = 1
AnnotationAtts.axesArray.ticksVisible = 1
AnnotationAtts.axesArray.autoSetTicks = 1
AnnotationAtts.axesArray.autoSetScaling = 1
AnnotationAtts.axesArray.lineWidth = 0
AnnotationAtts.axesArray.axes.title.visible = 1
AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.title.font.scale = 1
AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.title.font.bold = 0
AnnotationAtts.axesArray.axes.title.font.italic = 0
AnnotationAtts.axesArray.axes.title.userTitle = 0
AnnotationAtts.axesArray.axes.title.userUnits = 0
AnnotationAtts.axesArray.axes.title.title = ""
AnnotationAtts.axesArray.axes.title.units = ""
AnnotationAtts.axesArray.axes.label.visible = 1
AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.label.font.scale = 1
AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.label.font.bold = 0
AnnotationAtts.axesArray.axes.label.font.italic = 0
AnnotationAtts.axesArray.axes.label.scaling = 0
AnnotationAtts.axesArray.axes.tickMarks.visible = 1
AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
AnnotationAtts.axesArray.axes.grid = 0
SetAnnotationAttributes(AnnotationAtts)



DrawPlots()
