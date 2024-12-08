library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
-- moku_customwrap.vhd
-- Simplifed revision of the CustomWrapper interface 
entity moku_customwrap
    port (
        Clk : in std_logic; 			-- Clk and Reset
        Reset : in std_logic;			-- No surprises here
		--   Inputs (InputA,InputB) 		---
        InputA : in signed(15 downto 0); --   The Inputs to your custom instrument bitstream. 
        InputB : in signed(15 downto 0); --   These are always 16-bit ieee_numeric.signed vectors

		--   Outputs (OutputA,OutputB) 		---
        OutputA : out signed(15 downto 0); --   The Outputs from your custom instrument bitstream. 
        OutputB : out signed(15 downto 0); --   These are always 16-bit ieee_numeric.signed vectors
		
		-- Control Registers  				---
		-- Every moku instrument bitstream supports ten control registers 
		-- These are each 32 bit std_logic_vector's
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

