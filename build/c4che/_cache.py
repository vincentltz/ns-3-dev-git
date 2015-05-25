APPNAME = 'ns'
AR = '/usr/bin/ar'
ARFLAGS = 'rcs'
BINDIR = '/usr/local/bin'
BOOST_VERSION = '1_41'
BUILD_PROFILE = 'optimized'
BUILD_SUFFIX = '-optimized'
CC = ['/usr/bin/gcc']
CCDEFINES = []
CCFLAGS = ['-O3', '-g', '-Wall', '-Werror', '-O3', '-g', '-Wall', '-Werror', '-march=native', '-fstrict-overflow', '-Wno-error=deprecated-declarations', '-fstrict-aliasing', '-Wstrict-aliasing']
CCFLAGS_PTHREAD = '-pthread'
CCFLAGS_PYEXT = ['-fvisibility=hidden']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('4', '4', '7')
CFLAGS_GTK2 = ['-pthread', '-pthread']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_PYEMBED = ['-fno-strict-aliasing', '-fexceptions', '-fstack-protector', '-m64', '-mtune=generic', '-fPIC', '-fwrapv', '-fexceptions', '-fstack-protector', '-m64', '-mtune=generic', '-fPIC', '-fwrapv', '-fno-strict-aliasing']
CFLAGS_PYEXT = ['-pthread', '-fno-strict-aliasing', '-fexceptions', '-fstack-protector', '-m64', '-mtune=generic', '-fPIC', '-fwrapv', '-fexceptions', '-fstack-protector', '-m64', '-mtune=generic', '-fPIC', '-fwrapv', '-fno-strict-aliasing']
CFLAGS_cshlib = ['-fPIC']
COMPILER_CC = 'gcc'
COMPILER_CXX = 'g++'
CPPPATH_ST = '-I%s'
CXX = ['/usr/bin/g++']
CXXDEFINES = []
CXXFLAGS = ['-O3', '-g', '-Wall', '-Werror', '-march=native', '-fstrict-overflow', '-Wno-error=deprecated-declarations', '-fstrict-aliasing', '-Wstrict-aliasing']
CXXFLAGS_GTK2 = ['-pthread', '-pthread']
CXXFLAGS_MACBUNDLE = ['-fPIC']
CXXFLAGS_PTHREAD = '-pthread'
CXXFLAGS_PYEMBED = ['-fno-strict-aliasing', '-fexceptions', '-fstack-protector', '-m64', '-mtune=generic', '-fPIC', '-fwrapv', '-fexceptions', '-fstack-protector', '-m64', '-mtune=generic', '-fPIC', '-fwrapv', '-fno-strict-aliasing']
CXXFLAGS_PYEXT = ['-pthread', '-fno-strict-aliasing', '-fexceptions', '-fstack-protector', '-m64', '-mtune=generic', '-fPIC', '-fwrapv', '-fexceptions', '-fstack-protector', '-m64', '-mtune=generic', '-fPIC', '-fwrapv', '-fno-strict-aliasing', '-fvisibility=hidden', '-Wno-array-bounds']
CXXFLAGS_cxxshlib = ['-fPIC']
CXXLNK_SRC_F = []
CXXLNK_TGT_F = ['-o']
CXX_NAME = 'gcc'
CXX_SRC_F = []
CXX_TGT_F = ['-c', '-o']
DATADIR = '/usr/local/share'
DATAROOTDIR = '/usr/local/share'
DEFINES = ['HAVE_SYS_IOCTL_H=1', 'HAVE_IF_NETS_H=1', 'HAVE_NET_ETHERNET_H=1', 'HAVE_PACKET_H=1', 'HAVE_SQLITE3=1', 'HAVE_IF_TUN_H=1', 'HAVE_GSL=1']
DEFINES_PYEMBED = ['_GNU_SOURCE', 'NDEBUG', '_GNU_SOURCE']
DEFINES_PYEXT = ['_GNU_SOURCE', 'NDEBUG', '_GNU_SOURCE']
DEFINES_ST = '-D%s'
DEST_BINFMT = 'elf'
DEST_CPU = 'x86_64'
DEST_OS = 'linux'
DOCDIR = '/usr/local/share/doc/ns'
DOXYGEN = '/usr/bin/doxygen'
DVIDIR = '/usr/local/share/doc/ns'
ENABLE_BRITE = False
ENABLE_EMU = True
ENABLE_EXAMPLES = False
ENABLE_FDNETDEV = True
ENABLE_GSL = ' -lgsl -lgslcblas -lm  \n'
ENABLE_GTK2 = '-pthread -I/usr/include/gtk-2.0 -I/usr/lib64/gtk-2.0/include -I/usr/include/atk-1.0 -I/usr/include/cairo -I/usr/include/gdk-pixbuf-2.0 -I/usr/include/pango-1.0 -I/usr/include/glib-2.0 -I/usr/lib64/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12  -pthread -lgtk-x11-2.0 -lgdk-x11-2.0 -latk-1.0 -lgio-2.0 -lpangoft2-1.0 -lpangocairo-1.0 -lgdk_pixbuf-2.0 -lcairo -lpango-1.0 -lfreetype -lfontconfig -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lrt -lglib-2.0  \n'
ENABLE_LIBXML2 = '-I/usr/include/libxml2  -lxml2  \n'
ENABLE_NSC = False
ENABLE_PYTHON_BINDINGS = False
ENABLE_PYVIZ = False
ENABLE_REAL_TIME = True
ENABLE_STATIC_NS3 = False
ENABLE_SUDO = False
ENABLE_TAP = True
ENABLE_TESTS = False
ENABLE_THREADING = True
EXAMPLE_DIRECTORIES = ['energy', 'error-model', 'ipv6', 'matrix-topology', 'naming', 'realtime', 'routing', 'socket', 'stats', 'tcp', 'tutorial', 'udp-client-server', 'udp', 'wireless']
EXEC_PREFIX = '/usr/local'
HTMLDIR = '/usr/local/share/doc/ns'
INCLUDEDIR = '/usr/local/include'
INCLUDES_BOOST = '/usr/include'
INCLUDES_GTK2 = ['/usr/include/gtk-2.0', '/usr/lib64/gtk-2.0/include', '/usr/include/atk-1.0', '/usr/include/cairo', '/usr/include/gdk-pixbuf-2.0', '/usr/include/pango-1.0', '/usr/include/glib-2.0', '/usr/lib64/glib-2.0/include', '/usr/include/pixman-1', '/usr/include/freetype2', '/usr/include/libpng12']
INCLUDES_LIBXML2 = ['/usr/include/libxml2']
INCLUDES_PYEMBED = ['/usr/include/python2.6']
INCLUDES_PYEXT = ['/usr/include/python2.6']
INFODIR = '/usr/local/share/info'
INT64X64_USE_128 = 1
LIBDIR = '/usr/local/lib'
LIBEXECDIR = '/usr/local/libexec'
LIBPATH_BOOST = ['/usr/lib64']
LIBPATH_PYEMBED = ['/usr/lib64']
LIBPATH_PYEXT = ['/usr/lib64']
LIBPATH_PYTHON2.6 = ['/usr/lib64']
LIBPATH_ST = '-L%s'
LIB_BOOST = ['boost_system-mt', 'boost_signals-mt', 'boost_filesystem-mt']
LIB_GSL = ['gsl', 'gslcblas', 'm']
LIB_GTK2 = ['gtk-x11-2.0', 'gdk-x11-2.0', 'atk-1.0', 'gio-2.0', 'pangoft2-1.0', 'pangocairo-1.0', 'gdk_pixbuf-2.0', 'cairo', 'pango-1.0', 'freetype', 'fontconfig', 'gobject-2.0', 'gmodule-2.0', 'gthread-2.0', 'rt', 'glib-2.0']
LIB_LIBXML2 = ['xml2']
LIB_PYEMBED = ['python2.6']
LIB_PYEXT = ['python2.6']
LIB_PYTHON2.6 = ['python2.6']
LIB_RT = ['rt']
LIB_SQLITE3 = ['sqlite3']
LIB_ST = '-l%s'
LINKFLAGS_GTK2 = ['-pthread', '-pthread']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_PTHREAD = '-pthread'
LINKFLAGS_PYEMBED = []
LINKFLAGS_PYEXT = ['-pthread']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINKFLAGS_cxxshlib = ['-shared']
LINKFLAGS_cxxstlib = ['-Wl,-Bstatic']
LINK_CC = ['/usr/bin/gcc']
LINK_CXX = ['/usr/bin/g++']
LOCALEDIR = '/usr/local/share/locale'
LOCALSTATEDIR = '/usr/local/var'
MANDIR = '/usr/local/share/man'
MODULES_NOT_BUILT = ['brite', 'click', 'openflow', 'visualizer']
NS3_ENABLED_MODULES = ['ns3-antenna', 'ns3-aodv', 'ns3-applications', 'ns3-bridge', 'ns3-buildings', 'ns3-config-store', 'ns3-core', 'ns3-csma', 'ns3-csma-layout', 'ns3-dsdv', 'ns3-dsr', 'ns3-energy', 'ns3-fd-net-device', 'ns3-flow-monitor', 'ns3-internet', 'ns3-lr-wpan', 'ns3-lte', 'ns3-mesh', 'ns3-mobility', 'ns3-mpi', 'ns3-netanim', 'ns3-network', 'ns3-nix-vector-routing', 'ns3-olsr', 'ns3-point-to-point', 'ns3-point-to-point-layout', 'ns3-propagation', 'ns3-sixlowpan', 'ns3-spectrum', 'ns3-stats', 'ns3-tap-bridge', 'ns3-test', 'ns3-topology-read', 'ns3-uan', 'ns3-virtual-net-device', 'ns3-wave', 'ns3-wifi', 'ns3-wimax']
NS3_EXECUTABLE_PATH = ['/nfs/stak/students/l/liting/ns-3-dev-git/build/src/fd-net-device', '/nfs/stak/students/l/liting/ns-3-dev-git/build/src/tap-bridge']
NS3_MODULES = ['ns3-antenna', 'ns3-aodv', 'ns3-applications', 'ns3-bridge', 'ns3-buildings', 'ns3-config-store', 'ns3-core', 'ns3-csma', 'ns3-csma-layout', 'ns3-dsdv', 'ns3-dsr', 'ns3-energy', 'ns3-fd-net-device', 'ns3-flow-monitor', 'ns3-internet', 'ns3-lr-wpan', 'ns3-lte', 'ns3-mesh', 'ns3-mobility', 'ns3-mpi', 'ns3-netanim', 'ns3-network', 'ns3-nix-vector-routing', 'ns3-olsr', 'ns3-point-to-point', 'ns3-point-to-point-layout', 'ns3-propagation', 'ns3-sixlowpan', 'ns3-spectrum', 'ns3-stats', 'ns3-tap-bridge', 'ns3-test', 'ns3-topology-read', 'ns3-uan', 'ns3-virtual-net-device', 'ns3-wave', 'ns3-wifi', 'ns3-wimax']
NS3_MODULE_PATH = ['/usr/lib/gcc/x86_64-redhat-linux/4.4.7', '/nfs/stak/students/l/liting/ns-3-dev-git/build']
NS3_OPTIONAL_FEATURES = [('python', 'Python Bindings', False, 'PyBindGen missing'), ('brite', 'BRITE Integration', False, 'BRITE not enabled (see option --with-brite)'), ('nsclick', 'NS-3 Click Integration', False, 'nsclick not enabled (see option --with-nsclick)'), ('GtkConfigStore', 'GtkConfigStore', '-pthread -I/usr/include/gtk-2.0 -I/usr/lib64/gtk-2.0/include -I/usr/include/atk-1.0 -I/usr/include/cairo -I/usr/include/gdk-pixbuf-2.0 -I/usr/include/pango-1.0 -I/usr/include/glib-2.0 -I/usr/lib64/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12  -pthread -lgtk-x11-2.0 -lgdk-x11-2.0 -latk-1.0 -lgio-2.0 -lpangoft2-1.0 -lpangocairo-1.0 -lgdk_pixbuf-2.0 -lcairo -lpango-1.0 -lfreetype -lfontconfig -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lrt -lglib-2.0  \n', "library 'gtk+-2.0 >= 2.12' not found"), ('XmlIo', 'XmlIo', '-I/usr/include/libxml2  -lxml2  \n', "library 'libxml-2.0 >= 2.7' not found"), ('Threading', 'Threading Primitives', True, '<pthread.h> include not detected'), ('RealTime', 'Real Time Simulator', True, 'threading not enabled'), ('FdNetDevice', 'File descriptor NetDevice', True, 'FdNetDevice module enabled'), ('TapFdNetDevice', 'Tap FdNetDevice', True, 'Tap support enabled'), ('EmuFdNetDevice', 'Emulation FdNetDevice', True, 'Emulation support enabled'), ('PlanetLabFdNetDevice', 'PlanetLab FdNetDevice', False, 'PlanetLab operating system not detected (see option --force-planetlab)'), ('nsc', 'Network Simulation Cradle', False, 'NSC not found (see option --with-nsc)'), ('mpi', 'MPI Support', False, 'option --enable-mpi not selected'), ('openflow', 'NS-3 OpenFlow Integration', False, 'OpenFlow not enabled (see option --with-openflow)'), ('SqliteDataOutput', 'SQlite stats data output', ' -lsqlite3  \n', "library 'sqlite3' not found"), ('TapBridge', 'Tap Bridge', True, '<linux/if_tun.h> include not detected'), ('PyViz', 'PyViz visualizer', False, 'Python Bindings are needed but not enabled'), ('ENABLE_SUDO', 'Use sudo to set suid bit', False, 'option --enable-sudo not selected'), ('ENABLE_TESTS', 'Build tests', False, 'defaults to disabled'), ('ENABLE_EXAMPLES', 'Build examples', False, 'defaults to disabled'), ('GSL', 'GNU Scientific Library (GSL)', ' -lgsl -lgslcblas -lm  \n', 'GSL not found')]
OLDINCLUDEDIR = '/usr/include'
PACKAGE = 'ns'
PDFDIR = '/usr/local/share/doc/ns'
PKGCONFIG = '/usr/bin/pkg-config'
PLATFORM = 'linux2'
PREFIX = '/usr/local'
PRINT_BUILT_MODULES_AT_END = False
PSDIR = '/usr/local/share/doc/ns'
PYC = 1
PYCMD = '"import sys, py_compile;py_compile.compile(sys.argv[1], sys.argv[2])"'
PYFLAGS = ''
PYFLAGS_OPT = '-O'
PYO = 1
PYTHON = ['/usr/bin/python']
PYTHONARCHDIR = '/usr/local/lib64/python2.6/site-packages'
PYTHONDIR = '/usr/local/lib/python2.6/site-packages'
PYTHON_CONFIG = '/usr/bin/python-config'
PYTHON_VERSION = '2.6'
REQUIRED_BOOST_LIBS = ['system', 'signals', 'filesystem']
RPATH_ST = '-Wl,-rpath,%s'
SBINDIR = '/usr/local/sbin'
SHAREDSTATEDIR = '/usr/local/com'
SHLIB_MARKER = '-Wl,-Bdynamic'
SONAME_ST = '-Wl,-h,%s'
SQLITE_STATS = ' -lsqlite3  \n'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = '-Wl,-Bstatic'
STLIB_ST = '-l%s'
SUDO = '/usr/bin/sudo'
SYSCONFDIR = '/usr/local/etc'
VALGRIND = '/usr/bin/valgrind'
VALGRIND_FOUND = True
VERSION = '3-dev'
WL_SONAME_SUPPORTED = True
cfg_files = ['/nfs/stak/students/l/liting/ns-3-dev-git/build/ns3/config-store-config.h', '/nfs/stak/students/l/liting/ns-3-dev-git/build/ns3/core-config.h']
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
cxxprogram_PATTERN = '%s'
cxxshlib_PATTERN = 'lib%s.so'
cxxstlib_PATTERN = 'lib%s.a'
define_key = ['HAVE_SYS_IOCTL_H', 'HAVE_IF_NETS_H', 'HAVE_NET_ETHERNET_H', 'HAVE_IF_TUN_H', 'HAVE_PACKET_H', 'HAVE_SQLITE3', 'HAVE_GSL']
macbundle_PATTERN = '%s.bundle'
pyext_PATTERN = '%s.so'
