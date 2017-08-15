from conans import ConanFile, tools, os

class BoostGilConan(ConanFile):
    name = "Boost.Gil"
    version = "1.64.0"
    url = "https://github.com/bincrafters/conan-boost-gil"
    source_url = "https://github.com/boostorg/gil"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_name = "gil"
    requires =  "Boost.Bind/1.64.0@bincrafters/testing", \
                      "Boost.Concept_Check/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Iterator/1.64.0@bincrafters/testing", \
                      "Boost.Mpl/1.64.0@bincrafters/testing", \
                      "Boost.Preprocessor/1.64.0@bincrafters/testing", \
                      "Boost.Smart_Ptr/1.64.0@bincrafters/testing", \
                      "Boost.Static_Assert/1.64.0@bincrafters/testing", \
                      "Boost.Type_Traits/1.64.0@bincrafters/testing",\

                      #bind3 concept_check5 config0 core2 iterator5 mpl5 preprocessor0 smart_ptr4 static_assert1 type_traits3

    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.source_url))

    def package(self):
        include_dir = os.path.join(self.build_folder, self.lib_short_name, "include")
        self.copy(pattern="*", dst="include", src=include_dir)

    def package_id(self):
        self.info.header_only()