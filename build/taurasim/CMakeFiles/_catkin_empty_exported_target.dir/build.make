# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.28

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /opt/cmake-3.28.1-linux-x86_64/bin/cmake

# The command to remove a file.
RM = /opt/cmake-3.28.1-linux-x86_64/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/thxssio/projects/VSSS/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/thxssio/projects/VSSS/build

# Utility rule file for _catkin_empty_exported_target.

# Include any custom commands dependencies for this target.
include taurasim/CMakeFiles/_catkin_empty_exported_target.dir/compiler_depend.make

# Include the progress variables for this target.
include taurasim/CMakeFiles/_catkin_empty_exported_target.dir/progress.make

_catkin_empty_exported_target: taurasim/CMakeFiles/_catkin_empty_exported_target.dir/build.make
.PHONY : _catkin_empty_exported_target

# Rule to build all files generated by this target.
taurasim/CMakeFiles/_catkin_empty_exported_target.dir/build: _catkin_empty_exported_target
.PHONY : taurasim/CMakeFiles/_catkin_empty_exported_target.dir/build

taurasim/CMakeFiles/_catkin_empty_exported_target.dir/clean:
	cd /home/thxssio/projects/VSSS/build/taurasim && $(CMAKE_COMMAND) -P CMakeFiles/_catkin_empty_exported_target.dir/cmake_clean.cmake
.PHONY : taurasim/CMakeFiles/_catkin_empty_exported_target.dir/clean

taurasim/CMakeFiles/_catkin_empty_exported_target.dir/depend:
	cd /home/thxssio/projects/VSSS/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/thxssio/projects/VSSS/src /home/thxssio/projects/VSSS/src/taurasim /home/thxssio/projects/VSSS/build /home/thxssio/projects/VSSS/build/taurasim /home/thxssio/projects/VSSS/build/taurasim/CMakeFiles/_catkin_empty_exported_target.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : taurasim/CMakeFiles/_catkin_empty_exported_target.dir/depend
