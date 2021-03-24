echo "Patience"
cd src
julia --check-bounds=no -O3 runner.jl /opt/grids/quadtree/hdf5/point_345140.h5 128