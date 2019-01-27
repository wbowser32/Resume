import java.awt.*;
import javax.swing.*;
import java.awt.event.*;


public class Crisis2 extends JFrame implements ActionListener {
    JButton panicButton;
    JButton dontPanicButton;
    JButton blameButton;
    JButton mediaButton;
    JButton saveButton;
    JTextArea textArea;

    
    public Crisis2() {
        super("Crisis2");
        setLookAndFeel();
        setSize(348, 228);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        //FlowLayout flo = new FlowLayout();
        //setLayout(flo);
        BorderLayout b = new BorderLayout();
        setLayout(b);
        panicButton = new JButton("Panic");
        dontPanicButton = new JButton("Don't Panic");
        blameButton = new JButton("Blame Others");
        mediaButton = new JButton("Notify the Media");
        saveButton = new JButton("Save Yourself");
        textArea = new JTextArea("test");
        panicButton.addActionListener(this);dontPanicButton.addActionListener(this);
        blameButton.addActionListener(this);
        mediaButton.addActionListener(this);
        saveButton.addActionListener(this);

        JPanel p = new JPanel();
        
        JPanel[] panels = new JPanel[5];
        
        for(int i = 0 ; i < panels.length; i++)
        {
            panels[i] = new JPanel();
        }
        
        panels[0].add(panicButton);
        add(panels[0],BorderLayout.NORTH);
        
        panels[1].add(dontPanicButton);
        add(panels[1],BorderLayout.SOUTH);
        
        panels[2].add(blameButton);
        add(panels[2],BorderLayout.EAST);
       
        panels[3].add(mediaButton);
        panels[4].add(saveButton);
        
        p.add(panels[3]);
        p.add(panels[4]);
        
        add(p,BorderLayout.WEST);
        add(textArea,BorderLayout.CENTER);
        
        
        //p.add(panicButton);
        //p.add(dontPanicButton);
        //p.add(blameButton);
        //p.add(mediaButton);
        //p.add(saveButton);
        //add(textArea,BorderLayout.CENTER);
        //add(p,BorderLayout.NORTH);
        setVisible(true);
    }
    
    private void setLookAndFeel() 
    {
        try 
        {
            UIManager.setLookAndFeel
            (
                "com.sun.java.swing.plaf.nimbus.NimbusLookAndFeel"
            );  
            int x = 1;
        } 
        catch (Exception exc) 
        {
            int x = 1;
            //ignore error
        }
    }
    
    public void actionPerformed(ActionEvent e) 
    {
       String nText="";
       if(e.getSource() == panicButton)
       {
           nText = " we should panic";
       }
       else if(e.getSource() == dontPanicButton)
       {
           nText = "\"don't panic\"";
       }
       else if(e.getSource() == blameButton)
       {
           nText = "Point to the guy next to you";
       }
       else if(e.getSource() == mediaButton)
       {
           nText = "Sell the story to the media and get a bunker";
       }
       else if(e.getSource() == saveButton)
       {
           nText = "Save you life like a Final Fantasy game and hope for the best";
       }
       
       
       
       textArea.setText(nText);
    }
    
    public static void main(String[] arguments) 
    {
        Crisis2 cr = new Crisis2();
    }
}