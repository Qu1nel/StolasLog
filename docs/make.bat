@ECHO OFF
REM Command file for Sphinx documentation of StolasLog

pushd %~dp0

if "%1" == "" (
    echo.
    echo Please use "make ^<target^>" where ^<target^> is one of
    echo   html       to make standalone HTML files
    echo   livehtml   to build and watch for changes with live reload
    echo   clean      to remove all build files
    echo   ... and any other target supported by Sphinx.
    goto end
)

if "%1" == "livehtml" (
    echo.
    echo Starting live-reloading server...
    sphinx-autobuild source build/html --open-browser %SPHINXOPTS%
    goto end
)

REM For all other commands, pass them to sphinx-build
echo.
sphinx-build -M %1 source build %SPHINXOPTS%

:end
popd
