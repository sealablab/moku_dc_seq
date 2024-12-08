library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
-- moku_customwrap.vhd
-- Simplifed revision of the CustomWrapper interface 
entity moku_customwrap
    port (
        Clk : in std_logic;
        Reset : in std_logic;

        InputA : in signed(15 downto 0);
        InputB : in signed(15 downto 0);

        OutputA : out signed(15 downto 0);
        OutputB : out signed(15 downto 0);

        Control0 : in std_logic_vector(31 downto 0);
        Control1 : in std_logic_vector(31 downto 0);
        Control2 : in std_logic_vector(31 downto 0);
        Control3 : in std_logic_vector(31 downto 0)
    );
end entity;
-- # See Alsp
-- ## [CustomWrapper](https://compile.liquidinstruments.com/docs/wrapper.html#wrapper-ports)(EXT)
-- ## [CustomWrapper](https://publish.obsidian.md/sealablab/Lab/DevBoards/Moku/Moku-N/Moku-CustomWrapper)(Obsidian)

--

