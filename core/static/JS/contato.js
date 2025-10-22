function enviarWhats(){
    const nome = document.getElementById('nome').value;
    const assunto = document.getElementById('assunto').value;
    const telefone = '558491061685';
    const mensagem = document.getElementById('mensagem').value;
    const texto = `Olá, meu nome é ${nome}. Gostaria de falar sobre ${assunto}.: ${mensagem}`;
    const msgFormatada = encodeURIComponent(texto);
    const url = `https://wa.me/${telefone}?text=${msgFormatada}`;
    window.open(url, '_blank');

}
